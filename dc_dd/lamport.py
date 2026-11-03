import csv

with open('lamport.csv','r') as f:
    data = list(csv.DictReader(f))

clocks = {}
messages = {}

events = []

for d in data:
    eid = d['event_id']
    pid = d['process_id']
    type = d['event_type']
    msgTo = d['message_to']
    initClock = int(d['initial_clock'])

    if pid not in clocks:
        clocks[pid] = initClock

    old = clocks[pid]

    if type == "LOCAL":
        clocks[pid] += 1
        print("\n"
            f"{eid} | {pid} | Local |"
            f" L: {old} --> {clocks[pid]}"
        )

    elif type == "SEND":
        clocks[pid] += 1
        messages[msgTo] = clocks[pid]

        print("\n"
            f"{eid} | {pid} | Send --> {msgTo} |"
            f" L: {old} --> {clocks[pid]}"
        )

        print(
            f"Message TS : {clocks[pid]}"
        )

    else:
        t = messages.get(pid,0)
        clocks[pid] = max (
            clocks[pid],t
        ) + 1

        print("\n"
            f"{eid} | {pid} | RECEIVE | "
            f"L: max({old}, {t}) + 1 "
            f"= {clocks[pid]}"
        )

    events.append(
        {
            'event_id' : eid,
            'process_id' : pid,
            'event_type' : type,
            'clock' : clocks[pid]
        }
    )

events.sort(key = lambda x : (x['clock'],x['process_id']))

print ("\nEVents Order")
i = 1
for event in events:
    print(
        i,
        event["event_id"],
        event["process_id"],
        event["event_type"],
        "Clock =", event["clock"]
    )
    i += 1

print("\nClocks of all")
for i in clocks:
    print(
        f"{i} = {clocks[i]}"
    )