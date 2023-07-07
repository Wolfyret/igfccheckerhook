from requests_html import HTMLSession
session = HTMLSession()
import time
import configparser
config = configparser.ConfigParser()
config.add_section("data")
prob = '<a class="fc-login-button" href="/login">'
last='0'
from discord import Webhook, SyncWebhook
import aiohttp
import os.path
path = 'settings.ini'
check_file = os.path.isfile(path)
print(check_file)
while True:
    if check_file == True:
        r = session.get('https://www.indiegala.com/gameplay-giveaway')
        config.read('settings.ini')
        data = dict(config.items('data'))
        print(data)
        webhook = SyncWebhook.from_url(data['discordhooklink'])
        if prob in r.text:
            print('Live')
            if last!='live':
                webhook.send("IGFC is live :green_circle:")    
                last='live'
        else:
            print('Not live')
            if last!='not':
                webhook.send("IGFC is not live :red_circle:")  
                last ='not'

        time.sleep(int(data['time']))
    else:
        dchooklink = input('Your discord hook link: ')
        print('creating settings.ini')
        timerl = input('How often should it check? (you can change in settings.ini later) : ')
        config.set("data", "discordhooklink", dchooklink)
        config.set("data", "version", '0.0.2')
        config.set("data", "time", timerl)
        with open("settings.ini", 'w') as settings:
            config.write(settings)
        print('created, restart the program to continue')
        break
        
