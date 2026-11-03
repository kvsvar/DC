import csv
import random

with open('bully.csv','r') as f:
    data = list(csv.DictReader(f))

curr_cord = []
alive_nodes = []
#node_id,is_alive,is_current_coordinator
for d in data:
    if d['is_alive'] == "FALSE" and d['is_current_coordinator'] == "TRUE":
        curr_cord.append(d['node_id'])
    elif d['is_alive'] == "TRUE":
        alive_nodes.append(d['node_id'])

idx = random.randint(0,len(alive_nodes)-1)
initiator = alive_nodes[idx]

print(
    f"Node {initiator} ---> Leader Node {curr_cord[0]}"
    f"\nNo Response Timeout | Leader is Dead"
)

print(
    f"\nNode {initiator} Starts the Election !"
)

candidates = []

for d in data :
    if d['is_alive'] == "TRUE" and d['node_id'] > initiator:
        candidates.append(d['node_id'])
        print(
            f"\n[Election Msg] Node {initiator} --> Node {d['node_id']}"
            f"\n[Reply] Response OK"
        )
    elif d['is_alive'] == "FALSE" and d['node_id'] > initiator:
        print(
            f"\n[Election Msg] Node {initiator} --> Node {d['node_id']}"
            f"\n[Reply] No Response Timeout"
        )

for c in candidates.copy():
    print(
        f"\nNode {c} Starts the Election !"
    )
    for d in data :
        if d['is_alive'] == "TRUE" and d['node_id'] > c:
            print(
                f"\n[Election Msg] Node {c} --> Node {d['node_id']}"
                f"\n[Reply] Response OK"
            )
        elif d['is_alive'] == "FALSE" and d['node_id'] > c:
            print(
                f"\n[Election Msg] Node {c} --> Node {d['node_id']}"
                f"\n[Reply] No Response Timeout"
            )

leader = max(alive_nodes)

print(f"\n[COORDINATOR] Node {leader} becomes the new Leader")

for node in alive_nodes:
    if node != leader:
        print(
            f"[BROADCAST] Leader Node {leader} --> Node {node}"
        )