from configparser import SafeConfigParser
import argparse
from slack import Slack
from crowi import Crowi
import preprocess

if __name__ == '__main__':
    # load config
    config = SafeConfigParser()
    config.read('./config.ini', 'utf-8')
    slack_token = config.get('slack', 'token')
    crowi_url = config.get('crowi', 'url') 
    crowi_token = config.get('crowi', 'token')

    # get argument
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-n', '--channel-name', required=True, help='slack channel name')
    args = parser.parse_args()
    if args.channel_name:
        channel_name = args.channel_name

    # read messages from slack channel 
    s = Slack(slack_token)
    msgs = s.get_massages(channel_name)

    # convert to markdown format from message list
    msgs_table = preprocess.json2table(msgs)

    # write to crowi
    c = Crowi(crowi_url, crowi_token)
    c.update_page(channel_name, msgs_table)