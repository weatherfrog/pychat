#!/usr/bin/python3
# -*- coding: utf-8 -*-

# setting the pyhtonpath...
import _pythonpath

from datetime import datetime

from chatlib import (
    message_str, message_pretty_str, message_to_json, message_from_json,
    message_list_str, message_list_pretty_str, message_list_from_json,
    message_list_to_json)


def test0():
    message = {'from_user': 'calvin',
               'message': 'Look! A tiger!',
               'timestamp':  datetime.now()}
    print(message)
    print(message_str(message))
    print(message_pretty_str(message))
    print(message_to_json(message))
    json_str = message_to_json(message)
    message_clone = message_from_json(json_str)
    print(message_clone)


def test1():
    '''
    '''

    from datetime import timedelta
    timestamp = datetime(2017, 3, 21, 6, 0, 0)
    td = timedelta(minutes=3, seconds=13)

    message_list = []

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

    for i, msg in enumerate(msgs):
        message = {'from_user': msg[0], 'message': msg[1],
                   'timestamp': timestamp+i*td}
        message_list.append(message)

    print(message_list)
    print(message_list_str(message_list))
    print(message_list_pretty_str(message_list))
    json_str = message_list_to_json(message_list)
    message_list_clone = message_list_from_json(json_str)
    print(message_list_clone)

test0()
test1()
