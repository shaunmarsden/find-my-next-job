"""Unblind the paste test and add up the totals. Run with:
python3 evidence/paste-test/analyse.py evidence/paste-test
"""
import json, sys
from pathlib import Path
folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
ARMS = ("current", "inline", "none")
rows = []
for cid, m in mapping.items():
    s = scores[cid]
    assert s["scenario"] == m["scenario"], cid
    rows.append((m["scenario"], m["arm"], m["run"], cid, s))
for arm in ARMS:
    mine = [r for r in rows if r[1] == arm]
    right = sum(sum(r[4]["sort"]) for r in mine)
    strict = sum(sum(r[4].get("strict_sort", r[4]["sort"])) for r in mine)
    total = sum(len(r[4]["sort"]) for r in mine)
    shapes = [sum(r[4]["shape"]) for r in mine]
    print(f'{arm:8} replies={len(mine)} sorted right={right}/{total} (strict {strict}/{total}) '
          f'mean shape={sum(shapes)/len(shapes):.2f} full shape (6/6)={sum(1 for x in shapes if x == 6)} '
          f'failures={sum(r[4]["F"] for r in mine)}')
print()
for r in sorted(rows, key=lambda r: (r[0], ARMS.index(r[1]), r[2])):
    print(r[0], r[1], r[2], r[3], "sort", r[4]["sort"], "shape", r[4]["shape"])
