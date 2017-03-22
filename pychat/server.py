#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
simple chat server...
'''

from flask import Flask, request, render_template

from chatlib import message_list_to_json, message_from_json


app = Flask(__name__)


MESSAGE_LIST = []


@app.route('/')
def index():
    '''
    the main page...
    '''
    return render_template("webclient.html")


@app.route('/chat/post', methods=('POST', ))
def post_message():
    '''
    post a new message from a client
    '''

    app.logger.debug('post_message()')

    message = message_from_json(request.json)
    MESSAGE_LIST.append(message)

    return 'Message posted!'


@app.route('/chat/get_last_messages/<int:number_messages>')
def get_last_messages(number_messages):
    '''
    get number_messages last messages
    '''

    app.logger.debug(
        'get_last_messages(number_messages={})'.format(number_messages))

    message_list = MESSAGE_LIST[-number_messages:]

    return message_list_to_json(message_list)


@app.route('/chat/get_all_messages')
def get_all_messages():
    '''
    get all last messages
    '''

    app.logger.debug('get_all_last_messages')

    return message_list_to_json(MESSAGE_LIST)


if __name__ == "__main__":
    # will serve on http://127.0.0.1:5000/
    # you can navigate there with your browser

    import sys

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

