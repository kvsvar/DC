import csv

class TrustMeshServer:

    def processData (self,param):
        print(f"[Server] Process Parameter --> {param}")
        return param + 5


def invoke(server,methodName,param):
    method = getattr(server,methodName)

    return method(param)

with open('rpc.csv','r') as file:
    data = list(csv.DictReader(file))

server = TrustMeshServer()

for row in data:
    callID = row['call_id']
    client = row['client_name']
    methodName = row['method_name']
    param = row['param_value']
    ts = row['timestamp']

    print(f"\n[Invoke] {client} invoking {methodName}({param})")

    r = invoke(server,methodName,int(param))

    print(f"[Return] Result --> {r}")