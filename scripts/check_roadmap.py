#!/usr/bin/env python3
import argparse
import json
import math
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlsplit


FENCE = re.compile(r"^\s*(```|~~~)")
MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")
IGNORED_PARTS = {".git", ".venv", "__pycache__", "node_modules", "Mi-progreso"}


def basic_schema(data, issues):
    initial = len(issues)
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        issues.append("curriculum.json: schema_version debe ser 1")
        return False
    if not isinstance(data.get("modules"), list) or not isinstance(data.get("routes"), dict):
        issues.append("curriculum.json: modules debe ser lista y routes un objeto")
        return False
    required = {"id": str, "path": str, "title": str, "prerequisites": list, "hours": list, "category": str}
    for pos, item in enumerate(data["modules"]):
        if not isinstance(item, dict):
            issues.append(f"modules[{pos}]: debe ser objeto")
            continue
        for field, kind in required.items():
            if not isinstance(item.get(field), kind):
                issues.append(f"modules[{pos}].{field}: tipo inválido")
        if isinstance(item.get("prerequisites"), list) and any(not isinstance(x, str) for x in item["prerequisites"]):
            issues.append(f"modules[{pos}].prerequisites: IDs inválidos")
        hours = item.get("hours")
        valid_number = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)
        if isinstance(hours, list) and (len(hours) != 2 or any(not valid_number(x) or x < 0 for x in hours) or (len(hours) == 2 and all(valid_number(x) for x in hours) and hours[0] > hours[1])):
            issues.append(f"modules[{pos}].hours: rango inválido")
    for key, route in data["routes"].items():
        if not isinstance(key, str) or not isinstance(route, dict):
            issues.append("routes: entrada inválida")
            continue
        if not isinstance(route.get("title"), str) or not isinstance(route.get("path"), str) or not isinstance(route.get("modules"), list):
            issues.append(f"routes.{key}: tipo inválido")
        elif any(not isinstance(x, str) for x in route["modules"]):
            issues.append(f"routes.{key}.modules: IDs inválidos")
    return len(issues) == initial


def strip_fences(text):
    kept, inside, marker = [], False, ""
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            token = match.group(1)
            if not inside:
                inside, marker = True, token[0]
            elif token[0] == marker:
                inside = False
            kept.append("")
        else:
            kept.append("" if inside else line)
    return "\n".join(kept)


def markdown_targets(text):
    clean = strip_fences(text)
    for match in MD_LINK.finditer(clean):
        raw = match.group(1).strip()
        if raw.startswith("<") and raw.endswith(">"):
            raw = raw[1:-1]
        else:
            raw = raw.split(maxsplit=1)[0]
        yield raw, False
    yield from ((m.group(1).strip().removesuffix("\\"), True) for m in WIKILINK.finditer(clean))
    yield from ((m.group(1), False) for m in AUTOLINK.finditer(clean))


def local_target_exists(root, source, target_text, is_wikilink):
    candidates = []
    if is_wikilink:
        candidates.extend((root / target_text, source.parent / target_text))
        if "/" not in target_text:
            candidates.extend(root.rglob(target_text))
            candidates.extend(root.rglob(target_text + ".md"))
    else:
        candidates.append(root / target_text.lstrip("/") if target_text.startswith("/") else source.parent / target_text)
    for target in candidates:
        if target.exists() or (target.suffix == "" and target.with_suffix(".md").exists()):
            return True
    return False


def check_local_links(root, issues, external):
    urls = set()
    for source in root.rglob("*.md"):
        if any(part in IGNORED_PARTS for part in source.relative_to(root).parts):
            continue
        for raw, is_wikilink in markdown_targets(source.read_text(encoding="utf-8")):
            parts = urlsplit(raw)
            if parts.scheme in ("http", "https"):
                urls.add(raw)
                continue
            if parts.scheme or raw.startswith("#") or not parts.path:
                continue
            target_text = unquote(parts.path)
            if not local_target_exists(root, source, target_text, is_wikilink):
                issues.append(f"{source.relative_to(root)}: enlace local roto: {raw}")
    if external:
        check_external(urls, issues)


def check_external(urls, issues):
    for url in sorted(urls):
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "roadmap-link-check/1"})
        try:
            with urllib.request.urlopen(request, timeout=10) as response:
                if response.geturl() != url:
                    issues.append(f"WARNING: enlace externo redirige: {url} -> {response.geturl()}")
        except urllib.error.HTTPError as exc:
            if exc.code == 405:
                try:
                    request = urllib.request.Request(url, headers={"User-Agent": "roadmap-link-check/1", "Range": "bytes=0-0"})
                    with urllib.request.urlopen(request, timeout=10) as response:
                        if response.geturl() != url:
                            issues.append(f"WARNING: enlace externo redirige: {url} -> {response.geturl()}")
                    continue
                except urllib.error.HTTPError as get_exc:
                    exc = get_exc
                except (urllib.error.URLError, TimeoutError) as get_exc:
                    issues.append(f"WARNING: enlace externo no verificable (red): {url}: {get_exc}")
                    continue
            if exc.code in (401, 403, 429):
                issues.append(f"WARNING: enlace externo no verificable (acceso limitado {exc.code}): {url}")
            else:
                issues.append(f"enlace externo falló ({exc.code}): {url}")
        except (urllib.error.URLError, TimeoutError) as exc:
            issues.append(f"WARNING: enlace externo no verificable (red): {url}: {exc}")


def check_canvas(root, issues):
    for path in root.rglob("*.canvas"):
        if any(part in IGNORED_PARTS for part in path.relative_to(root).parts):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(f"{path.relative_to(root)}: canvas inválido: {exc}")
            continue
        nodes, edges = data.get("nodes", []), data.get("edges", [])
        if not isinstance(nodes, list) or not isinstance(edges, list) or any(not isinstance(x, dict) for x in nodes + edges):
            issues.append(f"{path.relative_to(root)}: schema canvas inválido")
            continue
        ids = [node.get("id") for node in nodes]
        if any(not isinstance(node_id, str) for node_id in ids) or len(ids) != len(set(ids)):
            issues.append(f"{path.relative_to(root)}: IDs de nodos inválidos o duplicados")
        known = set(ids)
        for node in nodes:
            if node.get("type") == "file" and isinstance(node.get("file"), str) and not (root / unquote(node["file"])).exists():
                issues.append(f"{path.relative_to(root)}: referencia canvas inexistente: {node['file']}")
        for edge in edges:
            if edge.get("fromNode") not in known or edge.get("toNode") not in known:
                issues.append(f"{path.relative_to(root)}: arista referencia nodo inexistente")


def check_roadmap(root: Path, external=False):
    root = root.resolve()
    issues = []
    try:
        data = json.loads((root / "curriculum.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"curriculum.json: {exc}"]
    if not basic_schema(data, issues):
        return issues
    ids = [m.get("id") for m in data["modules"] if isinstance(m, dict)]
    if len(ids) != len(set(ids)):
        issues.append("curriculum.json: IDs de módulos duplicados")
    by_id = {m.get("id"): m for m in data["modules"] if isinstance(m, dict) and isinstance(m.get("id"), str)}
    for mid, item in by_id.items():
        if not (root / item["path"]).exists():
            issues.append(f"módulo {mid}: path inexistente: {item['path']}")
        for prereq in item.get("prerequisites", []):
            if prereq not in by_id:
                issues.append(f"módulo {mid}: prerrequisito inexistente: {prereq}")
    visiting, done = set(), set()
    def visit(mid):
        if mid in visiting:
            issues.append(f"dependencias: ciclo detectado en {mid}")
            return
        if mid in done or mid not in by_id:
            return
        visiting.add(mid)
        for pre in by_id[mid].get("prerequisites", []): visit(pre)
        visiting.remove(mid); done.add(mid)
    for mid in by_id: visit(mid)
    for key, route in data["routes"].items():
        if not isinstance(route, dict) or not isinstance(route.get("modules"), list):
            issues.append(f"ruta {key}: schema inválido"); continue
        if len(route["modules"]) != len(set(route["modules"])):
            issues.append(f"ruta {key}: ID de módulo duplicado")
        if not isinstance(route.get("path"), str) or not (root / route.get("path", "")).exists():
            issues.append(f"ruta {key}: path inexistente: {route.get('path')}")
        seen = set()
        for mid in route["modules"]:
            if mid not in by_id:
                issues.append(f"ruta {key}: módulo inexistente: {mid}"); continue
            for pre in by_id[mid].get("prerequisites", []):
                if pre not in seen:
                    issues.append(f"ruta {key}: prerrequisito {pre} debe aparecer antes de {mid}")
            seen.add(mid)
    check_local_links(root, issues, external)
    check_canvas(root, issues)
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true")
    args = parser.parse_args()
    issues = check_roadmap(Path.cwd(), args.external)
    if issues:
        for issue in issues:
            print(issue if issue.startswith("WARNING:") else f"ERROR: {issue}")
        if any(not issue.startswith("WARNING:") for issue in issues):
            return 1
        return 0
    print("Roadmap válido."); return 0


if __name__ == "__main__":
    raise SystemExit(main())
