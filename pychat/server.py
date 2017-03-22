#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
simple chat server...
'''

from flask import request, render_template

from pychat.chatlib import message_list_to_json, message_from_json
from pychat import app


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
