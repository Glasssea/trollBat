import requests
import pandas as pd
from api_key import api_key
import time
import json

matchId = ""
matchId_list = []


data = pd.read_csv('csv/data.csv')
for i in data['matchId']:
    matchId_list.append(i)

for i in matchId_list:
    time.sleep(1.2)
    matchId = i

    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }

    response = requests.get(url, headers=headers)
    df = pd.DataFrame(response)

    df.to_csv(f'timeline/{matchId}.csv')

    data = response.json()
    with open(f'timeline/{matchId}.json', 'w') as f:
        json.dump(data, f)
    

    # print(df)



#match id 여러개 있으면 그거에 대한 time line을 다 가져옴
# 나중에 이 아래에다가 받아온 그 데이터들을 따로 또 수정하는 코드를 만들어 줘야 함(데이터 핸드링 하기 쉽게)

