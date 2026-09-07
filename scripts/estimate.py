#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Estima semanas de un ciclo de práctica.")
    parser.add_argument("--route", required=True)
    parser.add_argument("--hours", required=True, type=float, help="horas disponibles por semana")
    parser.add_argument("--completed", nargs="*", default=[])
    args = parser.parse_args()
    if not math.isfinite(args.hours) or args.hours <= 0:
        parser.error("--hours debe ser positivo")
    data = json.loads(Path("curriculum.json").read_text(encoding="utf-8"))
    if args.route not in data["routes"]:
        parser.error(f"ruta desconocida: {args.route}")
    route_ids = list(dict.fromkeys(data["routes"][args.route]["modules"]))
    unknown = sorted(set(args.completed) - set(route_ids))
    if unknown:
        parser.error("--completed solo admite módulos de la ruta: " + ", ".join(unknown))
    remaining = [mid for mid in route_ids if mid not in set(args.completed)]
    by_id = {m["id"]: m for m in data["modules"]}
    low = sum(by_id[mid]["hours"][0] for mid in remaining)
    high = sum(by_id[mid]["hours"][1] for mid in remaining)
    weeks_low, weeks_high = math.ceil(low / args.hours), math.ceil(high / args.hours)
    print(f"Ruta {args.route}: {low:g}–{high:g} horas; {weeks_low}–{weeks_high} semanas a {args.hours:g} h/semana.")
    print("Esta es una estimación de ciclo de práctica, no una afirmación de dominio ni de progreso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
