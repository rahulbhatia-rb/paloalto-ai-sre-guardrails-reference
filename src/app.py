"""JSONL interface for bounded AI remediation decisions."""
import json
import sys
from src.remediation import Signal, action


def evaluate(payload: dict) -> dict:
    return {"input": payload, "action": action(Signal(**payload))}


for line in sys.stdin:
    if line.strip():
        print(json.dumps(evaluate(json.loads(line))))
