import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock
import urllib.error


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from scripts.build_catalog import build_outputs, check_outputs, write_outputs
from scripts.check_roadmap import check_external, check_roadmap, markdown_targets


def module(mid, path, prerequisites=(), hours=(1, 2)):
    return {"id": mid, "path": path, "title": f"Modulo {mid}",
            "prerequisites": list(prerequisites), "hours": list(hours),
            "category": "test"}


class RoadmapFixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def save(self, modules, route_modules=None):
        for item in modules:
            path = self.root / item["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f'# {item["title"]}\n', encoding="utf-8")
        route_modules = route_modules if route_modules is not None else [m["id"] for m in modules]
        route_path = self.root / "routes/personal.md"
        route_path.parent.mkdir(exist_ok=True)
        route_path.write_text("Intro\n<!-- ROUTE:personal:START -->\nold\n<!-- ROUTE:personal:END -->\nFin\n", encoding="utf-8")
        data = {"schema_version": 1, "modules": modules,
                "routes": {"personal": {"title": "Personal", "path": "routes/personal.md", "modules": route_modules}}}
        (self.root / "curriculum.json").write_text(json.dumps(data), encoding="utf-8")
        return data


class ValidationTests(RoadmapFixture):
    def messages(self, modules, route=None):
        self.save(modules, route)
        return "\n".join(check_roadmap(self.root))

    def test_detects_missing_prerequisite(self):
        self.assertIn("prerrequisito inexistente", self.messages([module("a", "a.md", ["x"])]))

    def test_detects_dependency_cycle(self):
        text = self.messages([module("a", "a.md", ["b"]), module("b", "b.md", ["a"])])
        self.assertIn("ciclo", text)

    def test_route_requires_every_prerequisite_before_module(self):
        text = self.messages([module("a", "a.md"), module("b", "b.md", ["a"])], ["b", "a"])
        self.assertIn("antes de b", text)

    def test_markdown_decodes_percent20_and_reports_only_broken_link(self):
        data = self.save([module("a", "docs/A file.md")])
        source = self.root / data["modules"][0]["path"]
        source.write_text("[bien](A%20file.md)\n[mal](No%20existe.md)\n", encoding="utf-8")
        text = "\n".join(check_roadmap(self.root))
        self.assertNotIn("A%20file.md", text)
        self.assertIn("No%20existe.md", text)

    def test_ignores_links_in_fenced_examples_and_external_urls(self):
        data = self.save([module("a", "docs/a.md")])
        source = self.root / data["modules"][0]["path"]
        source.write_text("```md\n[ejemplo](missing.md)\n```\n[web](https://example.com/x)\n", encoding="utf-8")
        text = "\n".join(check_roadmap(self.root))
        self.assertNotIn("missing.md", text)
        self.assertNotIn("example.com", text)

    def test_canvas_checks_file_references_and_edge_nodes(self):
        self.save([module("a", "a.md")])
        canvas = {"nodes": [{"id": "n1", "type": "file", "file": "missing.md"}],
                  "edges": [{"id": "e1", "fromNode": "n1", "toNode": "n2"}]}
        (self.root / "map.canvas").write_text(json.dumps(canvas), encoding="utf-8")
        text = "\n".join(check_roadmap(self.root))
        self.assertIn("referencia canvas inexistente", text)
        self.assertIn("arista referencia nodo inexistente", text)

    def test_wikilinks_are_resolved_from_vault_root(self):
        data = self.save([module("a", "docs/a.md")])
        source = self.root / data["modules"][0]["path"]
        source.write_text("[[routes/personal]]\n", encoding="utf-8")
        self.assertNotIn("routes/personal", "\n".join(check_roadmap(self.root)))

    def test_malformed_schema_is_reported_without_crashing(self):
        (self.root / "curriculum.json").write_text(json.dumps({
            "schema_version": 1,
            "modules": [{"id": [], "path": 3, "title": "x", "prerequisites": [None],
                         "hours": [True, float("nan")], "category": "x"}],
            "routes": {},
        }), encoding="utf-8")
        issues = check_roadmap(self.root)
        self.assertTrue(issues)
        self.assertIn("tipo inválido", "\n".join(issues))

    def test_ignores_personal_and_dependency_directories(self):
        self.save([module("a", "a.md")])
        for directory in ("Mi-progreso", ".venv", "__pycache__", "node_modules"):
            path = self.root / directory / "bad.md"
            path.parent.mkdir()
            path.write_text("[roto](missing.md)\n", encoding="utf-8")
        self.assertNotIn("bad.md", "\n".join(check_roadmap(self.root)))

    def test_extracts_http_autolinks_but_not_fenced_autolinks(self):
        found = list(markdown_targets("<https://example.com/a>\n```\n<https://bad.test>\n```"))
        self.assertIn(("https://example.com/a", False), found)
        self.assertNotIn(("https://bad.test", False), found)

    def test_external_redirect_and_antibot_are_warnings(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): return False
            def geturl(self): return "https://example.com/final"
        issues = []
        with mock.patch("urllib.request.urlopen", return_value=Response()):
            check_external({"http://example.com"}, issues)
        with mock.patch("urllib.request.urlopen", side_effect=urllib.error.HTTPError("u", 403, "", {}, None)):
            check_external({"https://blocked.test"}, issues)
        self.assertEqual(len(issues), 2)
        self.assertTrue(all(issue.startswith("WARNING:") for issue in issues))

    def test_rejects_duplicate_ids_in_route(self):
        self.assertIn("duplicado", self.messages([module("a", "a.md")], ["a", "a"]))

    def test_incomplete_canvas_schema_does_not_crash(self):
        self.save([module("a", "a.md")])
        (self.root / "bad.canvas").write_text('{"nodes": null, "edges": {}}', encoding="utf-8")
        self.assertIn("schema canvas inválido", "\n".join(check_roadmap(self.root)))


class GeneratedOutputTests(RoadmapFixture):
    def test_catalog_and_route_blocks_are_deterministic_and_checkable(self):
        data = self.save([module("a", "docs/A file.md", hours=(2, 3))])
        outputs = build_outputs(self.root, data)
        catalog = outputs[self.root / "00-MOC/Catalogo de modulos.md"]
        self.assertIn("docs/A%20file.md", catalog)
        route = outputs[self.root / "routes/personal.md"]
        self.assertTrue(route.startswith("Intro\n"))
        self.assertTrue(route.endswith("Fin\n"))
        self.assertIn("2–3 horas", route)
        self.assertTrue(check_outputs(outputs))
        write_outputs(outputs)
        self.assertFalse(check_outputs(outputs))


class EstimateCliTests(RoadmapFixture):
    def test_estimate_excludes_completed_route_modules(self):
        self.save([module("a", "a.md", hours=(8, 16)), module("b", "b.md", hours=(8, 8))])
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts/estimate.py"), "--route", "personal", "--hours", "8", "--completed", "a"],
            cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1–1 semanas", result.stdout)
        self.assertIn("ciclo de práctica", result.stdout)

    def test_estimate_rejects_non_finite_hours(self):
        self.save([module("a", "a.md")])
        for value in ("nan", "inf", "0"):
            result = subprocess.run(
                [sys.executable, str(REPO / "scripts/estimate.py"), "--route", "personal", "--hours", value],
                cwd=self.root, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0, value)


if __name__ == "__main__":
    unittest.main()
