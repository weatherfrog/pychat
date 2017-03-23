# pychat

Python chat for the Powercoders school


## Instructions

Create a Python 3 virtualenv. On Unix/Linux/MacOS:

```
virtualenv -p python3 venv
. venv/bin/activate
```

On Windows:

```
python.exe -m venv venv
venv\Scripts\activate
```

Then install requirements:

```
pip install -r requirements.txt
```

Start the server:

```
python pychat/server.py 0.0.0.0
```

Start the client in a different terminal (don't forget to activate the virtual
environment again):

```
python pychat/client.py 0.0.0.0
```

Start chatting:

```
connecting to 0.0.0.0
      * 
      * Welcome to the "power.coders chat"!
      * 
      * if you are lost: call for "/help"
      * 
      * What is your desired user name? John
      * 
available commands are:
    - /help: print help (the one you are looking at).
    - /quit: quit the chat.
    - /poll [<number_messages>]: get all (or <number_messages>) from the server
    everything else will be posted.

chat> Hello!
11:44:15 John:
    Hello!

chat> 
```

The Python command line client is very basic. You have to poll for new messages
manually:

```
chat> /poll
11:44:15 John:
    Hello!
```

We'll create a Web-based client 
