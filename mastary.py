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
import time


api_key = "RGAPI-268ea45d-ed50-41e4-b46d-8a4c80696583" # riot developer에서 받아온 api_key 값 넣어주기, 24시간 마다 바꿔줘야 할 것임
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
'Aatrox (Aatrox)': 266,
'Ahri (Ahri)': 103,
'Akali (Akali)': 84,
'Akshan (Akshan)': 166,
'Alistar (Alistar)': 12,
'Amumu (Amumu)': 32,
'Anivia (Anivia)': 34,
'Annie (Annie)': 1,
'Aphelios (Aphelios)': 523,
'Ashe (Ashe)': 22,
'Aurelion Sol (AurelionSol)': 136,
'Azir (Azir)': 268,
'Bard (Bard)': 432,
'Bel\'Veth (Belveth)': 200,
'Blitzcrank (Blitzcrank)': 53,
'Brand (Brand)': 63,
'Braum (Braum)': 201,
'Caitlyn (Caitlyn)': 51,
'Camille (Camille)': 164,
'Cassiopeia (Cassiopeia)': 69,
'Cho\'Gath (Chogath)': 31,
'Corki (Corki)': 42,
'Darius (Darius)': 122,
'Diana (Diana)': 131,
'Draven (Draven)': 119,
'Dr. Mundo (DrMundo)': 36,
'Ekko (Ekko)': 245,
'Elise (Elise)': 60,
'Evelynn (Evelynn)': 28,
'Ezreal (Ezreal)': 81,
'Fiddlesticks (Fiddlesticks)': 9,
'Fiora (Fiora)': 114,
'Fizz (Fizz)': 105,
'Galio (Galio)': 3,
'Gangplank (Gangplank)': 41,
'Garen (Garen)': 86,
'Gnar (Gnar)': 150,
'Gragas (Gragas)': 79,
'Graves (Graves)': 104,
'Gwen (Gwen)': 887,
'Hecarim (Hecarim)': 120,
'Heimerdinger (Heimerdinger)': 74,
'Illaoi (Illaoi)': 420,
'Irelia (Irelia)': 39,
'Ivern (Ivern)': 427,
'Janna (Janna)': 40,
'Jarvan IV (JarvanIV)': 59,
'Jax (Jax)': 24,
'Jayce (Jayce)': 126,
'Jhin (Jhin)': 202,
'Jinx (Jinx)': 222,
'Kai\'Sa (Kaisa)': 145,
'Kalista (Kalista)': 429,
'Karma (Karma)': 43,
'Karthus (Karthus)': 30,
'Kassadin (Kassadin)': 38,
'Katarina (Katarina)': 55,
'Kayle (Kayle)': 10,
'Kayn (Kayn)': 141,
'Kennen (Kennen)': 85,
'Kha\'Zix (Khazix)': 121,
'Kindred (Kindred)': 203,
'Kled (Kled)': 240,
'Kog\'Maw (KogMaw)': 96,
'K\'Sante (KSante)': 897,
'LeBlanc (Leblanc)': 7,
'Lee Sin (LeeSin)': 64,
'Leona (Leona)': 89,
'Lillia (Lillia)': 876,
'Lissandra (Lissandra)': 127,
'Lucian (Lucian)': 236,
'Lulu (Lulu)': 117,
'Lux (Lux)': 99,
'Malphite (Malphite)': 54,
'Malzahar (Malzahar)': 90,
'Maokai (Maokai)': 57,
'Master Yi (MasterYi)': 11,
'Milio (Milio)': 902,
'Miss Fortune (MissFortune)': 21,
'Wukong (MonkeyKing)': 62,
'Mordekaiser (Mordekaiser)': 82,
'Morgana (Morgana)': 25,
'Naafiri (Naafiri)': 950,
'Nami (Nami)': 267,
'Nasus (Nasus)': 75,
'Nautilus (Nautilus)': 111,
'Neeko (Neeko)': 518,
'Nidalee (Nidalee)': 76,
'Nilah (Nilah)': 895,
'Nocturne (Nocturne)': 56,
'Nunu & Willump (Nunu)': 20,
'Olaf (Olaf)': 2,
'Orianna (Orianna)': 61,
'Ornn (Ornn)': 516,
'Pantheon (Pantheon)': 80,
'Poppy (Poppy)': 78,
'Pyke (Pyke)': 555,
'Qiyana (Qiyana)': 246,
'Quinn (Quinn)': 133,
'Rakan (Rakan)': 497,
'Rammus (Rammus)': 33,
'Rek\'Sai (RekSai)': 421,
'Rell (Rell)': 526,
'Renata Glasc (Renata)': 888,
'Renekton (Renekton)': 58,
'Rengar (Rengar)': 107,
'Riven (Riven)': 92,
'Rumble (Rumble)': 68,
'Ryze (Ryze)': 13,
'Samira (Samira)': 360,
'Sejuani (Sejuani)': 113,
'Senna (Senna)': 235,
'Seraphine (Seraphine)': 147,
'Sett (Sett)': 875,
'Shaco (Shaco)': 35,
'Shen (Shen)': 98,
'Shyvana (Shyvana)': 102,
'Singed (Singed)': 27,
'Sion (Sion)': 14,
'Sivir (Sivir)': 15,
'Skarner (Skarner)': 72,
'Sona (Sona)': 37,
'Soraka (Soraka)': 16,
'Swain (Swain)': 50,
'Sylas (Sylas)': 517,
'Syndra (Syndra)': 134,
'Tahm Kench (TahmKench)': 223,
'Taliyah (Taliyah)': 163,
'Talon (Talon)': 91,
'Taric (Taric)': 44,
'Teemo (Teemo)': 17,
'Thresh (Thresh)': 412,
'Tristana (Tristana)': 18,
'Trundle (Trundle)': 48,
'Tryndamere (Tryndamere)': 23,
'Twisted Fate (TwistedFate)': 4,
'Twitch (Twitch)': 29,
'Udyr (Udyr)': 77,
'Urgot (Urgot)': 6,
'Varus (Varus)': 110,
'Vayne (Vayne)': 67,
'Veigar (Veigar)': 45,
'Vel\'Koz (Velkoz)': 161,
'Vex (Vex)': 711,
'Vi (Vi)': 254,
'Viego (Viego)': 234,
'Viktor (Viktor)': 112,
'Vladimir (Vladimir)': 8,
'Volibear (Volibear)': 106,
'Warwick (Warwick)': 19,
'Xayah (Xayah)': 498,
'Xerath (Xerath)': 101,
'Xin Zhao (XinZhao)': 5,
'Yasuo (Yasuo)': 157,
'Yone (Yone)': 777,
'Yorick (Yorick)': 83,
'Yuumi (Yuumi)': 350,
'Zac (Zac)': 154,
'Zed (Zed)': 238,
'Zeri (Zeri)': 221,
'Ziggs (Ziggs)': 115,
'Zilean (Zilean)': 26,
'Zoe (Zoe)': 142,
'Zyra (Zyra)': 143
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
# data_df.to_csv('mastary_.csv', index=False)
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
