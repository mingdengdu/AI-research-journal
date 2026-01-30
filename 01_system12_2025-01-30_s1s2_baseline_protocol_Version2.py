#!/usr/bin/env python3
"""
Minimal experiment runner template.
- Parameterized via CLI args or config file
- Writes data/results.json with structured metrics
- Exit code 0 on success, non-zero on failure
"""

import argparse
import json
import random
import sys
from datetime import datetime
from pathlib import Path

def run_experiment(config):
    # TODO: replace with real training/eval code
    random.seed(config.get("seed", 0))
    # fake metric for demonstration
    metric = 0.7 + random.random() * 0.1
    return {"metric": metric, "timestamp": datetime.utcnow().isoformat() + "Z"}

def main():
    parser = argparse.ArgumentParser(description="Run a reproducible experiment and write results.json")
    parser.add_argument("--config", type=str, help="path to json config")
    parser.add_argument("--out", type=str, default="data/results.json", help="output results path")
    parser.add_argument("--seed", type=int, default=0, help="random seed")
    args = parser.parse_args()

    # load config if provided
    config = {}
    if args.config:
        try:
            with open(args.config, "r") as f:
                config = json.load(f)
        except Exception as e:
            print("Failed to read config:", e, file=sys.stderr)
            sys.exit(3)

    config["seed"] = args.seed

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        results = run_experiment(config)
        # enrich results with meta
        results["_meta"] = {
            "config": config,
            "exit": "success"
        }
        with open(out_path, "w") as f:
            json.dump(results, f, indent=2)
        print("Wrote results to", out_path)
        sys.exit(0)
    except Exception as e:
        err = {"error": str(e), "_meta": {"config": config, "exit": "failure"}}
        with open(out_path, "w") as f:
            json.dump(err, f, indent=2)
        print("Experiment failed:", e, file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()