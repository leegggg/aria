ariaurl = "http://aria2.lan.linyz.net:6800/jsonrpc"

def main():
    import requests, json
    from pprint import pprint
    jsondata = {
        "jsonrpc":"2.0",
        "id":"QXJpYU5nXzE1NDgzODg5MzhfMC4xMTYyODI2OTExMzMxMzczOA==",
    }

    reqdata = jsondata
    reqdata["method"] = "aria2.tellActive"
    param = []
    param.append("token:P)O(I*U&")
    reqdata["params"] = param
    ret = requests.post(ariaurl, json=reqdata)
    running = ret.json()
    
    pass



if __name__ == "__main__":
    main()