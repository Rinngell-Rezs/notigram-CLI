#Library import
import json, requests, sys, os

class InvalidTokenError(Exception):
# "This is a class that inherits from the Exception class, and it's called InvalidTokenError."
# 
# Throws and exception when api can't resolve with the given token
    pass

def ping(token:str,message:str):
    """
    It takes a token and a message and sends it to the server
    
    :param token: The token you got from the bot
    :type token: str
    :param message: The message you want to send
    :type message: str
    :return: A string containing the response from the server.
    """
    req = json.dumps({"token": token,"message": message}).encode('utf8')
    res = requests.post('https://notigram.up.railway.app/sendMessage',data=req)
    print(res.text)
    if('error' in res.text):
        raise InvalidTokenError(f"The token {token} doesn't exist or is not valid anymore.")
    return res.text

if __name__ == "__main__":
    # It's calling the function ping with the first and second argument of the command line.
    ping(sys.argv[1],' '.join(sys.argv[2:]))