"""Unblind the checker-line test and add up the totals. Run with:
python3 evidence/checker-line-test/analyse.py evidence/checker-line-test
"""
import json, sys
from pathlib import Path
folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
for arm in ("current", "fixed"):
    default = [c for c, m in mapping.items() if m["arm"] == arm and m["scenario"] != "warehouse-detail"]
    detail = [c for c, m in mapping.items() if m["arm"] == arm and m["scenario"] == "warehouse-detail"]
    for c in default + detail:
        assert scores[c]["scenario"] == mapping[c]["scenario"], c
    shapes = [sum(scores[c]["shape"]) for c in default]
    print(f'{arm:8} checker mentioned={sum(scores[c]["checker"] for c in default)}/{len(default)} '
          f'sorted right={sum(sum(scores[c]["sort"]) for c in default)}/{sum(len(scores[c]["sort"]) for c in default)} '
          f'mean shape={sum(shapes) / len(shapes):.2f} '
          f'said how it checked={sum(scores[c]["how"] for c in detail)}/{len(detail)} '
          f'failures={sum(scores[c]["F"] for c in default)}')
print()
for c, m in sorted(mapping.items(), key=lambda kv: (kv[1]["scenario"], kv[1]["arm"], kv[1]["run"])):
    print(m["scenario"], m["arm"], m["run"], c, scores[c])
