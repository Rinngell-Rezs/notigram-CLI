Notigram-CLI 🛎
===============

Notigram is a small project, aimed as a productivity-aid tool.

The functionality provided is basically sending notifications from a script or command line, to a Telegram client, so you can be notified about any kind of event through it.

The tool is composed by 3 parts: 
  * A CLI interface, which can be used from command line, python module, or http request. 
  * A Telegram Bot, which will provide a personal token for the user and will deliver the notifications. 
  * And finally the API, which manages the message requests and the bot.

The API code can be found `here on my other repo <https://github.com/Rinngell-Rezs/notigram-bot-API>`_, in case you want to check out how it works ^^.

The Telegram bot can be found as @notigram_apibot or at https://t.me/notigram_apibot.

Installing 👨‍💻
================

.. code-block:: bash

    pip install notigram

Usage 👓
=========

.. code-block:: bash

    >>> from notigram import ping
    >>> ping('<TOKEN>',"You've got a message from python!")
    {'response':'result'}

or 🤷‍♂️

.. code-block:: bash

    [user@linux ~]$ python -m notigram <TOKEN> Hello from command line! :D
    {'response':'result'}

If you aren't using a python program or a command line, you can always send an http post request to the server (https://notigram.blahaj-bay.gay/sendMessage) as well with the following format: 

.. code-block:: bash

    {
        "token": "TOKEN",
        "message": "The Postman says Hello!"
    }
