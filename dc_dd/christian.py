import csv

with open('christian.csv','r') as f:
    data = list(csv.DictReader(f))

for d in data:
    cid = d['client_id']
    t0 = int(d['t0_send_ms'])
    tS = int(d['t_server_ms'])
    t1 = int(d['t1_recv_ms'])

    rtt = t1 - t0
    estTime = tS + (rtt/2)
    offset = estTime - t1

    print(f"\n{cid}")
    print(f"t0: {t0} | t1: {t1} | tS: {tS}")
    print(f"RTT = {t1} - {t0} = {rtt} ms")
    print(f"Estimated Time = {tS} + ({rtt}/2) = {estTime} ms")
    print(f"Offset = {estTime} - {t1} = {offset} ms")
    
