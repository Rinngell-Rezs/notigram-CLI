import html, json, requests, sys


class InvalidTokenError(Exception):
    pass

class EmptyMessageError(Exception):
    pass

def ping(token:str, message:str):
    """
    It receives a token and a message and sends them to the Notigram API
    
    :param token: The token you got from the bot
    :type token: str
    :param message: The message you want to send
    :type message: str
    :return: A string containing the response from the server.
    """
    req = json.dumps({
        "token": token,
        "message": html.escape(message)
    }).encode('utf8')
    res = requests.post('https://notigram.blahaj-bay.gay/sendMessage', data=req)

    if('Invalid token' in res.text):
        raise InvalidTokenError(f"The token {token} doesn't exist or is not valid anymore.")
    elif('Message text is empty' in res.text):
        raise EmptyMessageError("Message is empty. Cannot send.")
    
    return res.text

if __name__ == "__main__":
    """Calls the function ping with the first and second argument from the command line."""
    res = ping(sys.argv[1],' '.join(sys.argv[2:]))
    print(res)
