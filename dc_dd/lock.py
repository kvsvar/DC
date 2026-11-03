import csv
import threading
import time

with open('lock.csv','r') as f:
    data = list(csv.DictReader(f))

lock = threading.Lock()
completed = []

def processTask (task):
    tid = task['task_id']
    threadName = task['thread_name']
    burst = int(task['burst_ms'])
    priority = task['priority']

    print(f"[THREAD] {threadName} started task {tid}")
    print(f"[WAITING] {threadName} waiting for lock -> {tid}")

    with lock:

        print(f"[Lock Acquired] {threadName} --> {tid}")
        print(
            f"[PROCESSING] {threadName} processing "
            f"{tid} | Priority: {priority}"
        )

        time.sleep(burst/1000)

        completed.append(task)

        print(f"[COMPLETED] {tid}")

        print(f"[LOCK RELEASED] {threadName} -> {tid}")

thread = []

for task in data:
    t = threading.Thread(
        target=processTask,
        args=(task,)
    )

    thread.append(t)
    t.start()

for t in thread:
    t.join()

print("\n===== FINAL COMPLETED TASKS =====")

for task_id in completed:
    print(task_id)