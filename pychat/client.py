#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
a command-line client for the powercoders chat
'''

from urllib.parse import urljoin
import requests
from datetime import datetime

from chatlib import (
    message_list_pretty_str, message_to_json,
    message_list_from_json)


class ChatShell:
    '''
    very primitive chat repl shell as client.
    '''

    PROMPT = 'chat> '
    INDENT = len(PROMPT) * ' '

    HELP = '''available commands are:
    - /help: print help (the one you are looking at).
    - /quit: quit the chat.
    - /poll [<number_messages>]: get all (or <number_messages>) from the server
    everything else will be posted.
'''

    def __init__(self, server, user=None):
        '''
        server = 'http://127.0.0.1:5000/' (or alike)
        user = 'calvin'
        '''

        self.server = server
        self.user = user

    def run(self):
        '''
        run the user input loop
        '''

        star_indent = ChatShell.INDENT + '* '

        print(star_indent)
        print(star_indent + 'Welcome to the "power.coders chat"!')
        print(star_indent)
        print(star_indent + 'if you are lost: call for "/help"')
        print(star_indent)

        if self.user is None:
            self.user = input(star_indent + 'What is your desired user name? ')
            print(star_indent)

        print(ChatShell.HELP)

        user_input = ''
        while True:
            user_input = input(ChatShell.PROMPT)
            if user_input.lower() == '/quit':
                break
            if user_input.lower() == '/help':
                print(ChatShell.HELP)
            elif user_input.lower().startswith('/poll'):
                split = user_input.split()
                if len(split) > 2:
                    print(star_indent + 'use "/poll" or "/poll <number>" ')
                    continue
                if len(split) == 1:
                    message_list = self.get_last_messages()
                    print(message_list_pretty_str(message_list))
                else:
                    try:
                        number_messages = int(split[1])
                        if number_messages <= 0:
                            raise ValueError('{} <= 0'.format(number_messages))
                    except ValueError:
                        print(star_indent + '"/poll <number>" accepts positive'
                              ' integers only!')
                        continue
                    message_list = self.get_last_messages(number_messages)
                    print(message_list_pretty_str(message_list))
            else:
                self.post_message(user_input)
                message_list = self.get_last_messages(number_messages=1)
                print(message_list_pretty_str(message_list))

        print('quitting, really? ok, bye!')

    def post_message(self, user_message):
        '''
        post message on the server
        '''

        message = {'from_user': self.user, 'message': user_message}
        uri = urljoin(self.server, '/chat/post')
        req = requests.post(uri, json=message_to_json(message))
        return req.text

    def get_last_messages(self, number_messages=None):
        '''
        '''

        uri = None
        if number_messages is not None:
            uri = urljoin(self.server,
                          '/chat/get_last_messages/{}'.format(number_messages))
        else:
            uri = urljoin(self.server,
                          '/chat/get_all_messages')
        req = requests.get(uri)

        message_list = message_list_from_json(req.text)
        return message_list


if __name__ == '__main__':

    import sys

    def main(args=None):
        '''
        '''

        if len(sys.argv) == 1:
            ip = '127.0.0.1'
        elif len(sys.argv) == 2:
            ip = sys.argv[1]
        else:
            print('usage: {} [ip]'.format(sys.argv[0]))
            sys.exit(255)
        print('connecting to {}'.format(ip))

        chat_shell = ChatShell(server='http://{}:8080'.format(ip))

        chat_shell.run()

    main()
