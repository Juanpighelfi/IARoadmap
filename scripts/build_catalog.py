#!/usr/bin/env python3
import argparse
import json
import os
import re
from pathlib import Path


def link_from(source: Path, target: Path) -> str:
    return os.path.relpath(target, source.parent).replace(os.sep, "/").replace(" ", "%20")


def route_block(root: Path, route_path: Path, route: dict, modules: dict) -> str:
    selected = [modules[mid] for mid in route["modules"]]
    low = sum(item["hours"][0] for item in selected)
    high = sum(item["hours"][1] for item in selected)
    lines = [f"**Carga orientativa:** {low}–{high} horas.", "",
             "Los prerrequisitos aparecen antes del módulo que los requiere.", ""]
    for item in selected:
        target = root / item["path"]
        lines.append(f'- [{item["title"]}]({link_from(route_path, target)}) — {item["hours"][0]}–{item["hours"][1]} horas')
    return "\n".join(lines) + "\n"


def replace_route_block(text: str, key: str, generated: str) -> str:
    start = f"<!-- ROUTE:{key}:START -->"
    end = f"<!-- ROUTE:{key}:END -->"
    pattern = re.compile(rf"({re.escape(start)})\s*.*?\s*({re.escape(end)})", re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"faltan marcadores de ruta {key}")
    return pattern.sub(lambda match: f"{match.group(1)}\n{generated}{match.group(2)}", text, count=1)


def build_outputs(root: Path, data: dict) -> dict[Path, str]:
    root = root.resolve()
    by_id = {item["id"]: item for item in data["modules"]}
    catalog_path = root / "00-MOC/Catalogo de modulos.md"
    rows = ["# Catálogo de módulos", "", "<!-- Generado desde curriculum.json; no editar a mano. -->", "",
            "| ID | Módulo | Categoría | Horas | Prerrequisitos |", "| --- | --- | --- | ---: | --- |"]
    for item in data["modules"]:
        prereqs = ", ".join(item["prerequisites"]) or "—"
        rows.append(f'| {item["id"]} | [{item["title"]}]({link_from(catalog_path, root / item["path"])}) | {item["category"]} | {item["hours"][0]}–{item["hours"][1]} | {prereqs} |')
    rows += ["", "## Rutas", "", "| Ruta | Horas |", "| --- | ---: |"]
    outputs = {}
    for key, route in data["routes"].items():
        selected = [by_id[mid] for mid in route["modules"]]
        low = sum(x["hours"][0] for x in selected)
        high = sum(x["hours"][1] for x in selected)
        route_path = root / route["path"]
        rows.append(f'| [{route["title"]}]({link_from(catalog_path, route_path)}) | {low}–{high} |')
        original = route_path.read_text(encoding="utf-8")
        outputs[route_path] = replace_route_block(original, key, route_block(root, route_path, route, by_id))
    outputs[catalog_path] = "\n".join(rows) + "\n"
    return outputs


def check_outputs(outputs: dict[Path, str]) -> list[str]:
    return [str(path) for path, expected in outputs.items()
            if not path.exists() or path.read_text(encoding="utf-8") != expected]


def write_outputs(outputs: dict[Path, str]) -> None:
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    data = json.loads((root / "curriculum.json").read_text(encoding="utf-8"))
    try:
        outputs = build_outputs(root, data)
    except (KeyError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}")
        return 1
    stale = check_outputs(outputs)
    if args.check:
        if stale:
            print("Archivos generados desactualizados:")
            print("\n".join(f"- {path}" for path in stale))
            return 1
        print("Catálogo y bloques de rutas actualizados.")
        return 0
    write_outputs(outputs)
    print("Catálogo y bloques de rutas generados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
