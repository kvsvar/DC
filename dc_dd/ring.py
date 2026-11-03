import csv
import random

with open('ring.csv','r') as f:
    data = list(csv.DictReader(f))

#node_id,next_node_id,is_active,priority_rank
dead = []
alive = []

for d in data:
    if d['is_active'] == "FALSE":
        dead.append(d['node_id'])
    else:
        alive.append(d['node_id'])

idx = random.randint(0,len(alive)-1)
initiator = alive[idx]

print(
    f"Node {initiator} ---> Leader Node {dead[0]}"
    f"\nNo Response Timeout | Leader is Dead"
)

print(
    f"\nNode {initiator} Starts the Election !"
)

candidates = []

curr = initiator

while True:
    for d in data:
        if d['node_id'] == curr:
            row = d
            break

    if row['is_active'] == "TRUE":
        print(
            f"\n[ELecttion Token] Election Token at Node {curr}"
        )
        candidates.append((row['node_id'],row['priority_rank']))
        curr = row['next_node_id']

    if row['is_active'] == "FALSE":
        curr = row['next_node_id']

    if curr == initiator:
        break

print("\nCandidates:", candidates)

leader = max(candidates, key=lambda x: (int(x[1]), int(x[0])))

print(f"\n[COORDINATOR] Node {leader[0]} becomes the new Leader")