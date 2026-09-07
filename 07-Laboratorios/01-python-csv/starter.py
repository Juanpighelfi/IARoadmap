"""Completa estas funciones y copia el archivo a Mi-progreso/labs/."""
import csv


def validate_rows(rows):
    """Devuelve (filas_validas, errores) para un iterable de diccionarios.

    Normaliza ID/material; convierte peso y dimensiones a float; rechaza IDs
    vacíos o repetidos y valores inválidos, no positivos o no finitos.
    """
    raise NotImplementedError


def read_and_validate(path):
    """Lee un CSV UTF-8 y devuelve el resultado de ``validate_rows``."""
    with open(path, newline="", encoding="utf-8") as stream:
        return validate_rows(csv.DictReader(stream))
