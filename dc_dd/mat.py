import csv
from multiprocessing import Pool

with open('matrix.csv','r') as f:
    data = list(csv.DictReader(f))

A = []

for row in data:
    A.append([
        int(row['col_0']),
        int(row['col_1']),
        int(row['col_2']),
        int(row['col_3'])
    ])

B = [
    [1,2],
    [2,3],
    [1,4],
    [3,1]
]

def multiply (task):
    worker, row_id, row = task

    print(f"[WORKER {worker}] Received row {row_id}")

    result = []

    for i in range(2):
        total = 0
        for j in range(4):
            total += row[j] * B[j][i]
        result.append(total)

    print(f"[WORKER {worker}] {row_id} -> {result}")
    
    return result

if __name__ == "__main__":

    tasks = []
    print("\n[MASTER] Scattering rows...")

    for i in range(len(A)):
        worker = (i%3) + 1
        print(f"[MASTER] Row {data[i]['row_id']} --> Worker {worker}")

        tasks.append([worker,data[i]['row_id'],A[i]])

    with Pool(3) as p:
        r = p.map(multiply,tasks)

    print("\n[MASTER] Gathering results...")
    
    print("\n===== FINAL MATRIX =====")
    for row in r:
        print(row)