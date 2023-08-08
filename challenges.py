#윤성찬 작업
import requests
import pandas as pd
from api_run.api_key import api_key

url = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1" #챌린저 소환사 아이디 가져오기 위해서  league-exp API사용

headers = { # request header
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}

response = requests.get(url, headers=headers) 
# print(response.json())


def get_challenges(api_key):
    url = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1"
    response = requests.get(url, headers=headers)
    return response.json()


data = get_challenges(api_key)

# Convert data to DataFrame
df = pd.DataFrame(data)
# print(df.columns)
# print(df)
# print(df["summonerId"])
summonerName = df["summonerName"]
print(summonerName)

# Save DataFrame to CSV
df.to_csv("challenges_test.csv")
