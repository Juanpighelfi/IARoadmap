"""Lectura y validación de un inventario sintético de piezas 3D."""
import csv
import math

NUMERIC_FIELDS = ("peso_g", "ancho_mm", "alto_mm", "profundidad_mm")
VALID_MATERIALS = {"PLA", "PETG", "ABS"}


def validate_rows(rows):
    """Separa filas válidas y errores sin detener el procesamiento del lote.

    ``rows`` es un iterable de diccionarios, como ``csv.DictReader``. Devuelve
    ``(validas, errores)``; los números de fila incluyen la cabecera CSV.
    """
    valid_rows = []
    error_reports = []
    accepted_ids = set()

    for row_number, row in enumerate(rows, start=2):
        errors = []
        piece_id = (row.get("pieza_id") or "").strip()
        material = (row.get("material") or "").strip().upper()

        if not piece_id:
            errors.append("pieza_id vacío")
        elif piece_id in accepted_ids:
            errors.append("pieza_id duplicado")
        if material not in VALID_MATERIALS:
            errors.append("material desconocido")

        clean_row = {"pieza_id": piece_id, "material": material}
        for field in NUMERIC_FIELDS:
            try:
                value = float(row.get(field, ""))
            except (TypeError, ValueError):
                errors.append(f"{field} no es numérico")
                continue
            clean_row[field] = value
            if not math.isfinite(value):
                errors.append(f"{field} debe ser finito")
            elif value <= 0:
                errors.append(f"{field} debe ser positivo")

        if errors:
            error_reports.append({"fila": row_number, "errores": errors})
        else:
            valid_rows.append(clean_row)
            accepted_ids.add(piece_id)

    return valid_rows, error_reports


def read_and_validate(path):
    """Lee un CSV UTF-8 desde newline='' y aplica ``validate_rows``."""
    with open(path, newline="", encoding="utf-8") as stream:
        return validate_rows(csv.DictReader(stream))
