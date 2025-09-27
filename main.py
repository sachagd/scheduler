import csv
from math import exp, log

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
contraintesf = parse_csv("contraintes.csv")

for i in range(len(contraintesf)):
    for j in range(1, len(contraintesf[i])):
        contraintesf[i][j] = contraintesf[i][j].split("-")

contraintes = {
    row[0]: set(
        s-1
        for j in range(1, len(row))
        for s in range(int(row[j][0]), int(row[j][1])+1)
    )
    for row in contraintesf
}

na = len(arows)
np = len(prows)

aindex = {arows[i][0]: i for i in range(na)}
pindex = {prows[i][0]: i for i in range(np)}

weights = [[0 for _ in range(na)] for _ in range(np)]

c = log(2.0)

for a in range(na):
    prefs = arows[a][1:]
    for r, pname in enumerate(prefs):
        weights[pindex[pname]][a] += exp(-c * r)

for p in range(np):
    prefs = prows[p][1:]
    for r, aname in enumerate(prefs):
        weights[p][aindex[aname]] += exp(-c * r)

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

allmeet = set(range(ncreneau))

for _, p, a in candidates:
    i = 0
    c = True
    while i < ncreneau:
        if nam[i] < nmeet:
            if (i in contraintes.get(prows[p][0], allmeet)) and (i in contraintes.get(arows[a][0], allmeet)):
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

authors_met = {a: set() for a in range(na)}
producers_met = {p: set() for p in range(np)}
for slot in meets:
    for p, a in slot:
        authors_met[a].add(p)
        producers_met[p].add(a)

auteurs_updated = []
for a in range(na):
    name = arows[a][0]
    prefs = arows[a][1:]
    met_names = {prows[p][0] for p in authors_met[a]}
    new_prefs = [x for x in prefs if x not in met_names]
    auteurs_updated.append([name] + new_prefs)

producteurs_updated = []
for p in range(np):
    name = prows[p][0]
    prefs = prows[p][1:]
    met_names = {arows[a][0] for a in producers_met[p]}
    new_prefs = [x for x in prefs if x not in met_names]
    producteurs_updated.append([name] + new_prefs)

with open("auteurs_updated.csv", "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f)
    wr.writerow(["name", "wishlist"])
    for row in auteurs_updated:
        wr.writerow([row[0]] + row[1:])

with open("producteurs_updated.csv", "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f)
    wr.writerow(["name", "wishlist"])
    for row in producteurs_updated:
        wr.writerow([row[0]] + row[1:])