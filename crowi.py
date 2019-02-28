import json
import requests

class Crowi(object):
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
    
    def get_page_list(self):
        url = self.base_url + '/_api/pages.list?access_token={}&path={}'
        r = requests.get(url.format(self.token, '/'))
        return r.json()['pages']
    
    def get_page_info(self, channel_name):
        path = '/slack/' + channel_name
        pages = self.get_page_list()
        page_info = {}
        for page in pages:
            if page['path'] == path:
                page_info = page
                break
        if page_info == {}:
            return None
        return page_info
    
    def get_page_content(self, channel_name):
        page_info = self.get_page_info(channel_name)
        url = self.base_url + '/_api/pages.get?access_token={}&path={}&page_id={}'
        r = requests.get(url.format(self.token, page_info['path'], page_info['id'], page_info['revision']))
        return r.json()
    
    def update_page(self, channel_name, body):
        page_info = self.get_page_info(channel_name)
        if page_info is None:
            return self.create_page(channel_name, body)
        payload = {
            'access_token': self.token,
            'page_id': page_info['id'],
            'revision_id': page_info['revision'],
            'body': body
        }

        url = self.base_url + '/_api/pages.update'
        r = requests.post(url, data=payload)
        if r.json()['ok'] is False:
            print('missing to update crowi page')
            return False
        return True
    
    def create_page(self, channel_name, body):
        payload = {
            'access_token': self.token,
            'path': '/slack/' + channel_name,
            'body': body
        }
        url = self.base_url + '/_api/pages.create'
        r = requests.post(url, data=payload)
        if r.json()['ok'] is False:
            print('missing to create crowi page')
            return False
        return True

    def filter_body(self, channel_name, body):
        now_body = self.get_page_content(channel_name)
        now_body = now_body['page']['revision']['body'].split('\n')
        body = body.split('\n')
        update_body = list(filter(lambda x: x not in now_body, body))
        new_body = [*now_body, *update_body]
        return '\n'.join(new_body)

if __name__ == '__main__':
    pass