import csv

with open('loadBal.csv','r') as f:
    data = list(csv.DictReader(f))

worker = [['W1',0], ['W2',0], ['W3',0]]
curr = 0

#job_id,compute_units,assigned_worker,status

for d in data:
    jid = d['job_id']
    units = int(d['compute_units'])
    worker[curr][1] += units

    print(
        f"\nJob {jid} --> Worker {worker[curr][0]}"
        f" | {worker[curr][0]} : {worker[curr][1]}"
    )

    curr = (curr+1) % len(worker)

print(worker)

worker = [['W1',0], ['W2',0], ['W3',0]]

#job_id,compute_units,assigned_worker,status

for d in data:
    jid = d['job_id']
    units = int(d['compute_units'])
    curr = min(worker, key = lambda x : x[1])

    curr[1] += units

    print(
        f"\nJob {jid} --> Worker {curr[0]}"
        f" | {curr[0]} : {curr[1]}"
    )

print(worker)

