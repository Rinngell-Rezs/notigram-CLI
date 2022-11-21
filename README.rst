Notigram-CLI
===============

Notigram is a small project, aimed exclusively as a productivity-aid tool.

The functionality provided is basically sending notifications from a script or command line, to a Telegram client, so you can be notified about any kind of event through it.

The tool is composed by 3 parts: A CLI interface, which can be used from command line, python module, or http request. A Telegram Bot, which will provide a personal token for the user and will deliver the notifications. And finally the API, which manages the message requests and the bot.

The API code can be found `here on my other repo <https://github.com/Rinngell-Rezs/notigram-bot-API>`_, in case you want to check out how it works ^^.

Installing
============

.. code-block:: bash

    pip install notigram

Usage
=====

.. code-block:: bash

    >>> from notigram import ping
    >>> ping('<TOKEN>',"You've got a message from python!")
    {'response':'result'}

or

.. code-block:: bash

    [user@linux ~]$ python -m notigram <TOKEN> Hello from command line! :D
    {'response':'result'}

If you aren't using a python program or a command line, you can always send an http post request to the server (https://notigram.up.railway.app/sendMessage) as well with the following format: 

.. code-block:: bash

    {
        "token": "TOKEN",
        "message": "Hello from a request!"
    }

Also, the text on the field message is parsed as HTML, so be careful when sending HTML formatting. This was done to make use of Telegram's text formatting when needed, which works as shown below:

.. code-block:: bash

    <b>Bold</b> 
    
    <i>Italic</i> 
    
    <u>Underline</u> 
    
    <s>Strikethrough</s> 
    
    <code>Monospaced text</code> 
    
    <pre>Monospaced paragraph</pre> 
    
    <tg-spoiler>Spoiler</tg-spoiler> 
    
    <a href="https://github.com/Rinngell-Rezs/notigram-CLI">Hyperlink</a> 

    <a href="tg://user?id=123456789">Inline mention of a Telegram user</a>