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
