#-*- coding:utf-8 -*-

import requests as req
import json
import re

accessToken = ''
app = ''

header = {'X-Line-Access': accessToken,
        'User-Agent': 'Line/9.2',
        'X-Line-Application': app,
        'Content-Type': 'application/json;charset=UTF-8'}

res = req.get('https://access.line.me/dialog/api/loginSession?locale=ja-JP', headers = header)

#print(res.json())

if res.json()['statusCode'] == 200:
    print('\033[32mApplications:\033[0m')
    if res.json()['result']['appLoginSessions'] != []:
        for devices in res.json()['result']['appLoginSessions']:
            print(f" \033[34m{devices['systemName']}\033[0m")
            print(f"   [sessionKey]: {devices['sessionKey']}")
            print(f"   [deviceType]: {devices['deviceType']['specificType']}")
            print(f"   [ipAddress]: {devices['ipAddress']}")
            print(f"   [location]: {devices['location']['fullDisplayText']}")
            print(f"   [loginTime]: {devices['latestLoginTime']['displayText']}\n")
    else:
        print(' empty')
    
    print('\033[32mwebApps:\033[0m')
    if res.json()['result']['webLoginSessions'] != []:
        for webapps in res.json()['result']['webLoginSessions']:
            print(f" \033[34m{webapps['browserType']}\033[0m")
            print(f"   [sessionKey]: {webapps['sessionKey']}")
            print(f"   [userAgent]: {webapps['userAgent']}")
            print(f"   [deviceType]: {webapps['deviceType']['specificType']}")
            print(f"   [ipAddress]: {webapps['ipAddress']}")
            print(f"   [location]: {webapps['location']['fullDisplayText']}")
            print(f"   [loginTime]: {webapps['latestLoginTime']['displayText']}\n")
    else:
        print(' empty')
else:
    print('\033[31mFailed\033[0m')


# req.post('https://access.line.me/dialog/api/loginSession/appSession/logout', headers=header, data = json.dumps({'sessionKey':'###sessionkey####'}))
# ^ kill one any device (maybe work...

# req.post('https://access.line.me/dialog/api/loginSession/webSession/logout', headers=header, data = json.dumps({'sessionKey':'####sessionkey####'}))
# ^ kill one any webApp (maybe work...

# req.post('https://access.line.me/dialog/api/loginSession/webSession/logoutAll', headers=header, data = json.dumps({}))
# ^ kill all webApp (maybe work...