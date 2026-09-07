import csv
import tempfile
import unittest
from pathlib import Path
from tests._loader import load
m = load(1, "01-python-csv")

class CSVTests(unittest.TestCase):
    def test_valid_and_invalid_rows(self):
        rows = [{"pieza_id":" P1 ","material":"PLA","peso_g":"12.5","ancho_mm":"10","alto_mm":"20","profundidad_mm":"3"},
                {"pieza_id":"","material":"ABS","peso_g":"-1","ancho_mm":"x","alto_mm":"2","profundidad_mm":"3"}]
        valid, errors = m.validate_rows(rows)
        self.assertEqual(valid[0]["pieza_id"], "P1")
        self.assertEqual(valid[0]["peso_g"], 12.5)
        self.assertEqual(errors[0]["fila"], 3)
        self.assertGreaterEqual(len(errors[0]["errores"]), 3)

    def test_duplicate_and_nonfinite_rejected(self):
        rows=[{"pieza_id":"A","material":"PETG","peso_g":"nan","ancho_mm":"1","alto_mm":"1","profundidad_mm":"1"},
              {"pieza_id":"A","material":"PLA","peso_g":"1","ancho_mm":"1","alto_mm":"1","profundidad_mm":"1"},
              {"pieza_id":"A","material":"PLA","peso_g":"2","ancho_mm":"1","alto_mm":"1","profundidad_mm":"1"}]
        valid, errors=m.validate_rows(rows)
        self.assertEqual(len(valid),1)
        self.assertTrue(any("finito" in e for e in errors[0]["errores"]))
        self.assertTrue(any("duplicado" in e for e in errors[-1]["errores"]))

    def test_read_csv_with_reordered_columns(self):
        fields = ["alto_mm", "pieza_id", "profundidad_mm", "material", "peso_g", "ancho_mm"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "piezas.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"pieza_id":"Z","material":"abs","peso_g":"5","ancho_mm":"4","alto_mm":"3","profundidad_mm":"2"})
            valid, errors = m.read_and_validate(path)
        self.assertEqual(errors, [])
        self.assertEqual(valid[0]["material"], "ABS")
