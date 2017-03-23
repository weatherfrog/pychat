#!/usr/bin/python3
# -*- coding: utf-8 -*-

# setting the pyhtonpath...
import _pythonpath

from urllib.parse import urljoin
import requests

from chatlib import message_to_json


def generate_messages(ip='127.0.0.1', port=8080):
    '''
    generate some test messages.
    '''

    from datetime import datetime, timedelta
    timestamp = datetime(2017, 3, 21, 6, 0, 0)
    td = timedelta(minutes=3, seconds=13)

    msgs = (
        ('calvin', 'Look! A tiger!'),
        ('hobbes', 'WHERE?!'),
        ('calvin', 'Wanna see something weird?'),
        ('calvin', ('Watch. You put bread in this slot and push down this '
                    'lever...')),
        ('calvin', 'Then in a few minutes, toast pops up!'),
        ('hobbes', 'Wow. Where does the bread go?'),
        ('calvin', "Beats me. Isn't that weird?"),
    )

    server = 'http://{}:{}/'.format(ip, port)
    uri = urljoin(server, '/chat/post')

    message_list = []

    for i, msg in enumerate(msgs):
        message = {'from_user': msg[0], 'message': msg[1],
                   'timestamp': timestamp+i*td}
        message_list.append(message)

        req = requests.post(uri, json=message_to_json(message))
        print(req.text)

generate_messages(ip='127.0.0.1', port=8080)
