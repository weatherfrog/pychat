# will serve on http://127.0.0.1:5000/
# you can navigate there with your browser

import sys

from pychat import app

# if an argument of the form '192.168.81.116' is given, it will be the
# address the server binds do

if len(sys.argv) == 1:
    ip = '127.0.0.1'
elif len(sys.argv) == 2:
    ip = sys.argv[1]
else:
    print('usage: {} [ip]'.format(sys.argv[0]))
    sys.exit(255)
print('binding to {}'.format(ip))

app.run(debug=True, host=ip, port=8080)

