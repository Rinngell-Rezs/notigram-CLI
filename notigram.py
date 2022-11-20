import json, requests, sys, os

class InvalidTokenError(Exception):
    pass

def ping(token:str,message:str):
    req = json.dumps({"token": token,"message": message}).encode('utf8')
    res = requests.post('http://localhost:8000/sendMessage/',data=req)
    if('error' in res.text):
        raise InvalidTokenError("The token you provided doesn't exists or is not valid anymore.")
    return res.text

if __name__ == "__main__":
    ping(sys.argv[1],sys.argv[2])