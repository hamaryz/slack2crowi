import re
from datetime import datetime, timezone, timedelta

def json2table(msgs):
    table = '| Date | User | Content |' + '\n'
    table += '|---|---|---|' + '\n'
    if type(msgs) is not list:
        msgs = list(msgs)
    for msg in msgs:
        row = '| ' + epoch2jst(msg['ts']).strftime('%Y-%m-%d %H:%M:%S') \
            + ' | ' + msg['user'] \
            + ' | ' + sanitize(msg['text'])
        table += row + '\n'
    return table

def sanitize(text):
    text = re.sub('\n', '<br>', text)
    text = re.sub('```', '', text)
    text = re.sub('<(http.+?)>', '\\1', text)
    return text

def epoch2jst(epoch_time):
    jst = timezone(timedelta(hours=+9), 'JST')
    loc = datetime.fromtimestamp(epoch_time, jst)
    return loc

# def extract_unregisted_message(msgs):
