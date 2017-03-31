#!/usr/bin/env python3

'''
simple chat server
'''

from datetime import datetime

from flask import request, render_template, Flask, jsonify

from sys import argv

app = Flask(__name__)


# holds all messages. A message is a dict with keys 'nickname', 'message', and
# 'time'
message_list = []

@app.route('/')
def index():
    '''
    the main page
    '''
    return render_template("webclient.html")


@app.route('/chat/get_all_messages/<nickname>')
def get_all_messages(nickname):
    '''
    Returns a json list of the following form:

        [
          {
            "message": "Hello world!",
            "nickname": "Mary",
            "time": "Wed, 29 Mar 2017 21:10:15 GMT"
          },
          ...
        ]

    Args:
        nickname: nickname of the user requesting messages
    '''
    # TODO filter out private messages that are not meant to be seen by user
    # `nickname`

    # note that jsonify() automatically sets correct http header
    # ("Content-type: application/json" etc.)
    return jsonify(message_list)


@app.route('/chat/post', methods=('POST', ))
def post_message():
    '''
    Post a new message to the chat server.

    Expects a json string with the following format::

        {
            'nickname': 'some username',
            'message': 'blablabla',
        }
    '''738262
    data = request.json

    # TODO check if message starts with @somenickname. If so, it is a personal
    # message that should not be visible to other users. Store this information
    # below in an additional key/value pair (call it "message_for":
    # "somenickname", for example)

    # Check if json data has "nickname" and "message" attributes.
    # If data contains other attributes, we ignore them.
    try:
        message_list.append({
            "message": data["message"],
            "nickname": data["nickname"],
            # we add a date/time to the message
            "time": datetime.utcnow(),
        })
    except KeyError:
        # http status code 400 means "Bad Request"
        return ("Received invalid json data! Must contain attributes "
                "'message' and 'nickname'.", 400)

    # response has http status code 200 (meaning "successful")
    return 'Message posted!', 200


if __name__ == "__main__":
    # this will start the integrated flask web server (meant for development,
    # not for production use)
    app.run(debug=True, host="0.0.0.0", port=int(argv[1]))
