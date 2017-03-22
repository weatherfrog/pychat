#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
stuff needed on the server and on the client.
'''

from datetime import datetime
import json


DATETIME_FMT = '%Y-%m-%d %H:%M:%S.%f'


def json_handler(obj):
    '''
    is called whenever json does not know how to handle an obj.

    for the moment datetime is the only issue
    '''

    if isinstance(obj, datetime):
        return {'__datetime__': obj.strftime(DATETIME_FMT)}
    else:
        msg = ('Object of type {} with value of {!r} is not JSON '
               'serializable').format(type(obj), obj)
        raise TypeError(msg)


def as_datetime(dct):
    '''
    de-serialize datetime
    '''

    if '__datetime__' in dct:
        return datetime.strptime(dct['__datetime__'], DATETIME_FMT)
    return dct


# message:
# a dictionary of the form
# message = {'from_user': 'calvin',
#            'message': 'Look! A tiger!',
#            'timestamp':  datetime.now()}

def message_str(message):
    '''
    str representation of a message
    '''

    fmt = '''Message:
    - from_user: {0[from_user]}
    - timestamp: {0[timestamp]}
    - message:   {0[message]!r}'''

    return fmt.format(message)


def message_pretty_str(message):
    '''
    str representation of a message
    '''

    fmt = '''{0[timestamp]:%H:%M:%S}@{0[from_user]}:
       {0[message]!r}'''
    return fmt.format(message)


def message_to_json(message):
    '''
    json representation of a message
    '''

    return json.dumps(message, default=json_handler)


def message_from_json(message):
    '''
    json representation of a message
    '''

    return json.loads(message, object_hook=as_datetime)


# message_list: just a list of messages (see above)

def message_list_str(message_list):
    '''
    str representation of a message_list
    '''

    ret = '\n'.join(message_str(message) for message in message_list)

    return ret


def message_list_pretty_str(message_list):
    '''
    str representation of a message_list
    '''

    ret = '\n'.join(message_pretty_str(message) for message in message_list)

    return ret


def message_list_to_json(message_list):
    '''
    json representation of a message_list
    '''

    return json.dumps(message_list, default=json_handler)


def message_list_from_json(message_list):
    '''
    json representation of a message_list
    '''

    return json.loads(message_list, object_hook=as_datetime)
