import csv

def processData (param):
    print(f"[Server] Processing Parameter --> {param}")
    return param + 5

def dispatcher (methodName , param):
    if methodName == "processData":
        return processData(int(param))

    else:
        return "Unkown Method NAme"

with open('rpc.csv','r') as file:
    data = list(csv.DictReader(file))

for row in data:
    callID = row['call_id']
    client = row['client_name']
    methodName = row['method_name']
    param = row['param_value']
    ts = row['timestamp']

    print(f"\n[Dispatch] {ts} : Client Inovking Method : {client} --> {methodName}({param})")

    r = dispatcher(methodName,param)

    print(f"[Return] Result --> {r}")