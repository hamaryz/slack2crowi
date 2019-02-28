from configparser import SafeConfigParser

slack_token = input('input slack token: ')
crowi_token = input('input crowi token: ')
crowi_url = input('input crowi URL(including http or https): ')

config = SafeConfigParser()

section_slack = 'slack'
config.add_section(section_slack)
config.set(section_slack, 'token', slack_token)

section_crowi = 'crowi'
config.add_section(section_crowi)
config.set(section_crowi, 'token', crowi_token)
config.set(section_crowi, 'url', crowi_url)

with open('config.ini', 'w') as f:
    config.write(f)