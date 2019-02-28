import re
import json
import requests
import time
from datetime import datetime, timezone, timedelta

class Slack(object):
    def __init__(self, token):
        self.user_list = []
        self.token = token

    def get_channel_id(self, channel_name):
        url = 'https://slack.com/api/channels.list?token={}'
        r = requests.get(url.format(self.token))
        channel_id = [ch['id'] for ch in r.json()['channels'] if ch['name'] == channel_name] 
        return channel_id[0]

    def get_channel_history(self, channel_id):
        url = 'https://slack.com/api/channels.history?token={}&channel={}'
        r = requests.get(url.format(self.token, channel_id))
        if r.json()['ok'] is not True:
            print('missing to get messages')
            return r.json()
        return r.json()['messages']

    def get_user_list(self):
        url = 'https://slack.com/api/users.list?token={}'
        r = requests.get(url.format(self.token))
        if r.json()['ok'] is not True:
            print('missing to get messages')
            return r.json()
        return r.json()['members']

    def resolve_user(self, user_id):
        if self.user_list == []:
            self.user_list = self.get_user_list()
        user_name = [user['real_name'] for user in self.user_list if user['id'] == user_id]
        return user_name[0]
    
    def get_massages(self, channel_name):
        channel_id = self.get_channel_id(channel_name)
        channel_history = self.get_channel_history(channel_id)

        msgs = []
        for msg in channel_history:
            if msg['type'] != 'message':
                continue
            try:
                msgs.append({
                    'user': self.resolve_user(msg['user']),
                    'text': msg['text'],
                    'ts': float(msg['ts'])
                })
            except KeyError:
                pass
        msgs = self.clean_messages(msgs)
        msgs = sorted(msgs, key=lambda x:x['ts'])
        return msgs
    
    def clean_messages(self, msgs):
        cleaned_msgs = []
        pattern = 'has joined the channel|set the channel purpose'
        for msg in msgs:
            if re.search(pattern, msg['text']):
                continue
            cleaned_msgs.append(msg)
        return cleaned_msgs

if __name__ == '__main__':
    pass