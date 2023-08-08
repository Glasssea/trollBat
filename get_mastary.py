# 이 파일 사용법 encryptedSummonerId를 가져와서 변수에 넣어주고 실행하면 바로 이 사람의 5랩(파이썬에선 5랩이 롤에선 7랩임)
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')

import requests #리퀘스트 임포트
import pandas as pd #판다스 임포트하고 축약어 설정
import time  #타임모듈 설정 / time.sleep 때문에(api요청에 제한이 있는데 그걸 지키지 않으면 밴 먹기 때문에)

from api_key import api_key #api_key 재사용성을 높이는 방법 알아냄
# api_key = "RGAPI-627e8271-05a9-45f3-907a-4992c91468e3" # riot developer에서 받아온 api_key 값 넣어주기, 24시간 마다 바꿔줘야 할 것임
ranking_id_url = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1" # champion rank 해서 1위부터 랭킹정보 뽑아오기 위한 url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
response = requests.get(ranking_id_url, headers=headers)
challenger_id = pd.DataFrame(response.json())
print(challenger_id.columns) #columns이름 알아내기
time.sleep(1)


# challenger_id = pd.read_csv('idsCH.csv')


print(challenger_id) # request 받은 랭킹 순위 dataframe으로 만들어서 그냥 바로 출력한 것이고
print(challenger_id.index) #이건 그것의 인덱스가 몇까지 있는지(즉, 몇위까지 있는지 알려주는 것임) range함수로 줌
champion = { #챔피언 인덱스번호 딕셔너리 / 이대로 사용하면 불편해서 아래에 이 dictionary의 key, value 값을 바꿔줄 거임
'Aatrox': 266,
'Ahri': 103,
'Akali': 84,
'Akshan': 166,
'Alistar': 12,
'Amumu': 32,
'Anivia': 34,
'Annie': 1,
'Aphelios': 523,
'Ashe': 22,
'Aurelion Sol': 136,
'Azir': 268,
'Bard': 432,
"Bel'Veth": 200,
'Blitzcrank': 53,
'Brand': 63,
'Braum': 201,
'Caitlyn': 51,
'Camille': 164,
'Cassiopeia': 69,
"Cho'Gath": 31,
'Corki': 42,
'Darius': 122,
'Diana': 131,
'Draven': 119,
'Dr. Mundo': 36,
'Ekko': 245,
'Elise': 60,
'Evelynn': 28,
'Ezreal': 81,
'Fiddlesticks': 9,
'Fiora': 114,
'Fizz': 105,
'Galio': 3,
'Gangplank': 41,
'Garen': 86,
'Gnar': 150,
'Gragas': 79,
'Graves': 104,
'Gwen': 887,
'Hecarim': 120,
'Heimerdinger': 74,
'Illaoi': 420,
'Irelia': 39,
'Ivern': 427,
'Janna': 40,
'Jarvan IV': 59,
'Jax': 24,
'Jayce': 126,
'Jhin': 202,
'Jinx': 222,
"Kai'Sa": 145,
'Kalista': 429,
'Karma': 43,
'Karthus': 30,
'Kassadin': 38,
'Katarina': 55,
'Kayle': 10,
'Kayn': 141,
'Kennen': 85,
"Kha'Zix": 121,
'Kindred': 203,
'Kled': 240,
"Kog'Maw": 96,
"K'Sante": 897,
'LeBlanc': 7,
'Lee Sin': 64,
'Leona': 89,
'Lillia': 876,
'Lissandra': 127,
'Lucian': 236,
'Lulu': 117,
'Lux': 99,
'Malphite': 54,
'Malzahar': 90,
'Maokai': 57,
'Master Yi': 11,
'Milio': 902,
'Miss Fortune': 21,
'Wukong': 62,
'Mordekaiser': 82,
'Morgana': 25,
'Naafiri': 950,
'Nami': 267,
'Nasus': 75,
'Nautilus': 111,
'Neeko': 518,
'Nidalee': 76,
'Nilah': 895,
'Nocturne': 56,
'Nunu & Willump': 20,
'Olaf': 2,
'Orianna': 61,
'Ornn': 516,
'Pantheon': 80,
'Poppy': 78,
'Pyke': 555,
'Qiyana': 246,
'Quinn': 133,
'Rakan': 497,
'Rammus': 33,
"Rek'Sai": 421,
'Rell': 526,
'Renata Glasc': 888,
'Renekton': 58,
'Rengar': 107,
'Riven': 92,
'Rumble': 68,
'Ryze': 13,
'Samira': 360,
'Sejuani': 113,
'Senna': 235,
'Seraphine': 147,
'Sett': 875,
'Shaco': 35,
'Shen': 98,
'Shyvana': 102,
'Singed': 27,
'Sion': 14,
'Sivir': 15,
'Skarner': 72,
'Sona': 37,
'Soraka': 16,
'Swain': 50,
'Sylas': 517,
'Syndra': 134,
'Tahm Kench': 223,
'Taliyah': 163,
'Talon': 91,
'Taric': 44,
'Teemo': 17,
'Thresh': 412,
'Tristana': 18,
'Trundle': 48,
'Tryndamere': 23,
'Twisted Fate': 4,
'Twitch': 29,
'Udyr': 77,
'Urgot': 6,
'Varus': 110,
'Vayne': 67,
'Veigar': 45,
"Vel'Koz": 161,
'Vex': 711,
'Vi': 254,
'Viego': 234,
'Viktor': 112,
'Vladimir': 8,
'Volibear': 106,
'Warwick': 19,
'Xayah': 498,
'Xerath': 101,
'Xin Zhao': 5,
'Yasuo': 157,
'Yone': 777,
'Yorick': 83,
'Yuumi': 350,
'Zac': 154,
'Zed': 238,
'Zeri': 221,
'Ziggs': 115,
'Zilean': 26,
'Zoe': 142,
'Zyra': 143
}

# 딕셔너리 뒤집기(챔피언번호 : 챔피언이름)
champion_reverse = {v: k for k, v in champion.items()}


data = [] # csv파일로 저장하기 위한 data 리스트

for i in challenger_id.index: # 랭킹 끝까지 for문 돌린다는 의미 ㅇㅋ? 37 line 참고 / 이 for문 돌 때 마다 한 순위의 유저에 대한 내용 탐구한다고 생각하면 됨
    time.sleep(1)
    print('랭킹', (i+1), '위')
    print('encryptedId : ', challenger_id.iloc[i]['summonerId']) #encrypted summoner id(자료 요청할 enc id)
    encryptedSummonerId = challenger_id.iloc[i]['summonerId'] # 이건 소환사닉네임을 암호화한 값임 다른 api정보에서 가져올 수 있음 / summoner에서 id 가 encryptedId임

    #mastary 정보를 encryptedSummonerId로 request하기 위한 url
    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}" # 암호화된 소환사 닉네임을 통해 그 유저의 챔피언 숙련도 확인할 수 있는 request url

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token" : api_key
    }

    response = requests.get(url, headers=headers)
    # print(response.json())
    df = pd.DataFrame(response.json())
    
    # 데이터프레임 출력('puuid', 'championId', 'championLevel', 'championPoints', 'lastPlayTime', 'championPointsSinceLastLevel', 'championPointsUntilNextLevel', 'chestGranted', 'tokensEarned', 'summonerId')
    # 컬럼 확인용
    # print(df.columns)
    
    level = 5 #숙련도 5만 뽑겠다 그런 거임 이거때문에 오류가 났던 것 같다.
    level_index = df[df["championLevel"]==level]
    # print(level_index[['championId']])

    mastary_df = df



    # 'championName' 컬럼 추가하고, champion 이름으로 변환된 값들을 넣어줌
    mastary_df['championName'] = mastary_df['championId'].map(champion_reverse)
    # print(challenger_id.iloc[i]['summonerName'])
    # print(mastary_df[['championId', 'championName', 'championLevel', 'championPoints']])
    # print('-'*80)
    # print('index가 뭥미',mastary_df.index)
    for j in mastary_df.index: 
        row = []  
        # print(challenger_id.iloc[i]['summonerName'])
        # print('확인')
        # print(j)
        # print(mastary_df.iloc[j])
        row.append(challenger_id.iloc[i]['summonerName'])
        row.append(mastary_df.iloc[j]['championId'])
        row.append(mastary_df.iloc[j]['championName'])
        row.append(mastary_df.iloc[j]['championLevel'])
        row.append(mastary_df.iloc[j]['championPoints'])
        data.append(row)
    # print(data)

data_df = pd.DataFrame(data, columns=['summonerName', 'championId', 'championName','championLevel','championPoints'])
data_df.to_csv('mastary_2.csv', index=False)
# def save_to_csv(summoner_name):
#     champion_mastery = get_masteries(summoner_name)
#     data = []

#     for mastary_df in champion_mastery:
#         row = [
#             summoner_name,
            # mastary_df['championId'],
            # mastary_df['championName'],
            # mastary_df['championLevel'],
            # mastary_df['championPoints']
#         ]
#         data.append(row)

#     df = pd.DataFrame(data, columns=['SummonerName', 'ChampionId', 'ChampionName', 'ChampionLevel', 'ChampionPoints'])
#     df.to_csv(f'{summoner_name}_mastery.csv', index=False)
