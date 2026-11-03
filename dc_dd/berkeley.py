import csv

with open('berkeley.csv','r') as f:
    data = list(csv.DictReader(f))

faulty_nodes = []

sum = 0

for d in data:
    if d['is_faulty'] == "TRUE":
        faulty_nodes.append(d)

    else:
        sum += int(d['clock_time_sec'])

print(
    f"Faulty nodes:", [i["node_id"] for i in faulty_nodes]
)

nodes = int(len(data)) - int(len(faulty_nodes))
avg = sum/nodes

print(
    f"\n[Master] Avg Cal | Sum = {sum} | Nodes = {nodes}"
    f"\n[Master] Avg = {sum}/{nodes} = {avg: .3f}"
)

for d in data:
    if d['is_faulty'] == "FALSE":
        print(f"\nNode {d['node_id']}")
        offset = avg - int(d['clock_time_sec'])
        print(f"Node Time = {d['clock_time_sec']} || Master = {avg: .3f}")
        print(f"Offset = {avg: .3f} - {d['clock_time_sec']} = {offset: .3f}")