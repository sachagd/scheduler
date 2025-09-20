import csv
from math import exp

def parse_csv(filepath, encoding="utf-8-sig"):
    with open(filepath, "r", encoding=encoding, newline="") as f:
        reader = csv.reader(f)
        next(reader, None)
        rows = []
        for row in reader:
            row = [c.strip() for c in row]
            while row and row[-1] == "":
                row.pop()
            if row:
                rows.append(row)
        return rows

arows = parse_csv("auteurs.csv")
prows = parse_csv("producteurs.csv") 

na = len(arows)
np = len(prows)

aindex = {arows[i][0]: i for i in range(na)}
pindex = {prows[i][0]: i for i in range(np)}

weights = [[0 for _ in range(na)] for _ in range(np)]

for i in range(na):
    for j in range(1,len(arows[i])):
        weights[pindex[arows[i][j]]][i] += exp(3 * (na - j) / na) 

for i in range(np):
    for j in range(1,len(prows[i])):
        weights[i][aindex[prows[i][j]]] += exp(3 * (np - j) / np)

with open("ncreneau.txt", "r", encoding="utf-8") as f:
    ncreneau = int(f.read().strip()) # nombre de créneaux
nmeet = 18 # nombre de réunion en même temps

candidates = []
for p in range(np):
    for a in range(na):
        w = weights[p][a]
        if w > 0.0:
            candidates.append((w, p, a))

candidates.sort(reverse=True)

nam = [0 for _ in range(ncreneau)]
aam = [[] for _ in range(ncreneau)]
pam = [[] for _ in range(ncreneau)]
meets = [[] for _ in range(ncreneau)]
skipped = []

for _, p, a in candidates:
    i = 0
    c = True
    while i < ncreneau:
        if nam[i] < nmeet:
            if not (p in pam[i] or a in aam[i]):
                aam[i].append(a)
                pam[i].append(p)
                nam[i] += 1
                meets[i].append((p, a))
                c = False
                break
        i += 1
    if c:
        skipped.append((p, a))

with open("meetings.csv", "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f)
    
    max_meets = max(len(slot) for slot in meets)
    header = ["créneau"] + [f"meeting_{i+1}" for i in range(max_meets)]
    wr.writerow(header)
    
    for slot_idx, pairs in enumerate(meets, start=1):
        row = [slot_idx]
        for p, a in pairs:
            row.append(f"{prows[p][0]} - {arows[a][0]}")
        wr.writerow(row)

with open("skipped.txt", "w", encoding="utf-8-sig") as f:
    for p, a in skipped:
        f.write(f"{prows[p][0]} - {arows[a][0]}\n")