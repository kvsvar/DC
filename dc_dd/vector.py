import csv

with open('vector.csv','r') as f:
    data = list(csv.DictReader(f))

clocks = {
    'P1' : {
        'P1' : 0,
        'P2' : 0,
        'P3' : 0
    },
    'P2' : {
        'P1' : 0,
        'P2' : 0,
        'P3' : 0
    },
    'P3' : {
        'P1' : 0,
        'P2' : 0,
        'P3' : 0
    }
}

messages = {}
events = {}

#event_id,process_id,event_action,target_process

for e in data:
    eid = e['event_id']
    pid = e['process_id']
    type = e['event_action']
    msgTo = e['target_process']

    old = clocks[pid].copy()

    if type == "LOCAL":
        clocks[pid][pid] += 1
        print(
            f"\n{eid} | {pid} | LOCAL |"
            f"\nCLock: {old} --> {clocks[pid]}"
        )

    elif type == "SEND":
        clocks[pid][pid] += 1
        messages[msgTo] = clocks[pid].copy()
        print(
            f"\n{eid} | {pid} | SEND --> {msgTo} |"
            f"\nCLock: {old} --> {clocks[pid]}"
        )
        print(
            f"Message TS : {messages[msgTo]}"
        )

    else:
        t = messages.get(pid)

        for p in clocks:
            clocks[pid][p] = max(
                t[p],clocks[pid][p]
            )

        clocks[pid][pid] += 1

        print(
            f"\n{eid} | {pid} | Recieve |"
            f"\nCLock: max({old},{t}) + 1"
            f"\nClock: {clocks[pid]}"
        )
    events[eid] = {
        'process_id': pid,
        'event_type': type,
        'clock': clocks[pid].copy()
    }

print("\nEvents")
for e in events:
    print(
        f"{e} --> {events[e]['clock']}"
    )

print("\nProcess Wise Clocks")
for process in clocks:
    print(process, "=", clocks[process])