import pandas as pd
import json


#csv 불러오기인데 이거 말고 아래껄로 해서 해야할 듯 함
# data = pd.read_csv("timeline/KR_6561085084.csv")
print('start')
print('start')
print('start')
print('start')

matchId_list = []
data = pd.read_csv('csv/data.csv')
for i in data['matchId']:
    match_json = 'matches/'+i+'.json'
    matchId_list.append(match_json)

for matchId in matchId_list:
    pass
with open(matchId_list[9], 'r') as f:
    matches = json.load(f)

print(matchId_list[9])
print(matchId_list[9])

# print(type(pd.DataFrame(matches).loc['participants'].loc['info']))
# print(pd.DataFrame(matches).loc['participants'].loc['info'][0].get('win'))
# print(pd.DataFrame(matches).loc['participants'].loc['info'][0].get('championName'))
# print(pd.DataFrame(matches).loc['participants'].loc['info'][0].get('championId'))
# print(pd.DataFrame(matches).loc['participants'].loc['info'][0].get('participantId'))


champ =[]
champId = []
for i in range(10):#임시
    champ.append(pd.DataFrame(matches).loc['participants'].loc['info'][i].get('championName'))
    champId.append(pd.DataFrame(matches).loc['participants'].loc['info'][i].get('championId'))
# print(champ)

with open('timeline/KR_6601400285.json', 'r') as f:
    data = json.load(f)


df = pd.DataFrame(data)
# print(df.loc['frames']['info'][1].get('events')[1])

# for i in df.loc['frames']['info'][10].get('events'):
#     print(i)
# for i in df.loc['participants']['info'][1:]:
#     print(i)



info = df.iloc[4]['info']
xy_data = pd.DataFrame(info[0]['participantFrames']).loc['position']
time = info[1]['timestamp']

# print(time)

# puuid 저장
puuid_list = []
for i in df.iloc[2][1]:
    puuid_list.append(i.get('puuid'))
# print(puuid_list)

# 어느 팀이 이겼는지 확인 winningTeam
if info[-1]['events'][-1].get('winningTeam') == 100: 
    blue = 1
    red = 0
else:
    blue = 0
    red = 1

col = ['puuid', 'participantId', 'championId', 'championName', 'timestamp', 'position', 'win']

df_position = []

timeMin = 0
for i in range(len(info)):
    # print('time',i)    
    for j in range(1,11):
        row = []
        # print(i, info[i]['participantFrames'].get(str(j)).get('position'))
        row.append(puuid_list[j-1])
        row.append(j) # participantId(1,2,3,4,5,6,7,8,9,10)
        row.append(champId[j-1])
        row.append(champ[j-1])
        row.append(i)
        row.append([info[i]['participantFrames'].get(str(j)).get('position').get('x'),info[i]['participantFrames'].get(str(j)).get('position').get('y')])
        # row.append(info[i]['participantFrames'].get(str(j)).get('position').get('y'))
        if j<=5:
            row.append(red)
        else:
            row.append(blue)
        df_position.append(row)
# print(df_position)
df_position = pd.DataFrame(df_position, columns=col)
print(df_position)

#문제점 찾았음 동일한 챔피언이 상대편에 있음, 그게 문제인데 이 문제를 해결하려면 팀별로 나눠서 진행해야 할 것 같음 화딱지가 나는 것 같음.

champ_position = df_position.pivot(index='championId', columns='timestamp', values='position')
champN_position = df_position.pivot(index='championName', columns='timestamp', values='position')
user_position = df_position.pivot(index='participantId', columns='timestamp', values='position')


# print(champ_position)
# print(champN_position)
# print(champN_position.loc[champ[0]])
# print(champN_position.loc[champ[1]])
# print(champN_position.loc[champ[2]])
# print(user_position)

champion_dic = { #챔피언별 위치데이터(매 판 분 수 다를거임, 즉 컬럼 수 다를거임 / 패딩해서 넣어줘야 함 넣을 때)
'Aatrox': [],
'Ahri': [],
'Akali': [],
'Akshan': [],
'Alistar': [],
'Amumu': [], #
'Anivia': [],
'Annie': [],
'Aphelios': [],
'Ashe': [],
'AurelionSol': [],
'Azir': [],
'Bard': [],
"Bel'Veth": [],
'Blitzcrank': [],
'Brand': [],
'Braum': [],
'Caitlyn': [],
'Camille': [],
'Cassiopeia': [],
"Cho'Gath": [],
'Corki': [],
'Darius': [],
'Diana': [],
'Draven': [],
'Dr. Mundo': [],
'Ekko': [],
'Elise': [],
'Evelynn': [],
'Ezreal': [],
'FiddleSticks': [], #
'Fiora': [],
'Fizz': [],
'Galio': [],
'Gangplank': [],
'Garen': [],
'Gnar': [],
'Gragas': [],
'Graves': [],
'Gwen': [],
'Hecarim': [],
'Heimerdinger': [],
'Illaoi': [],
'Irelia': [],
'Ivern': [],
'Janna': [],
'JarvanIV': [],
'Jax': [],
'Jayce': [],
'Jhin': [],
'Jinx': [],
"Kaisa": [],
'Kalista': [],
'Karma': [],
'Karthus': [],
'Kassadin': [],
'Katarina': [],
'Kayle': [],
'Kayn': [],
'Kennen': [],
"Khazix": [],#
'Kindred': [],
'Kled': [],
"KogMaw": [],
"KSante": [],
'LeBlanc': [],
'LeeSin': [],
'Leona': [],
'Lillia': [],
'Lissandra': [],
'Lucian': [],
'Lulu': [],
'Lux': [],
'Malphite': [],
'Malzahar': [],
'Maokai': [],
'Master Yi': [],
'Milio': [],
'Miss Fortune': [],
'Wukong': [],
'Mordekaiser': [],
'Morgana': [],
'Naafiri': [],
'Nami': [],
'Nasus': [],
'Nautilus': [],
'Neeko': [],
'Nidalee': [],
'Nilah': [],
'Nocturne': [],
'Nunu': [],
'Olaf': [],
'Orianna': [],
'Ornn': [],
'Pantheon': [],
'Poppy': [],
'Pyke': [],
'Qiyana': [],
'Quinn': [],
'Rakan': [],
'Rammus': [],
"RekSai": [],
'Rell': [],
'RenataGlasc': [],
'Renekton': [],
'Rengar': [],
'Riven': [],
'Rumble': [],
'Ryze': [],
'Samira': [],
'Sejuani': [],
'Senna': [],
'Seraphine': [],
'Sett': [],
'Shaco': [],
'Shen': [],
'Shyvana': [],
'Singed': [],
'Sion': [],
'Sivir': [],
'Skarner': [],
'Sona': [],
'Soraka': [],
'Swain': [],
'Sylas': [],
'Syndra': [],
'Tahm Kench': [],
'Taliyah': [],
'Talon': [],
'Taric': [],
'Teemo': [],
'Thresh': [],
'Tristana': [],
'Trundle': [],
'Tryndamere': [],
'Twisted Fate': [],
'Twitch': [],
'Udyr': [],
'Urgot': [],
'Varus': [],
'Vayne': [],
'Veigar': [],
"Vel'Koz": [],
'Vex': [],
'Vi': [],
'Viego': [],
'Viktor': [],
'Vladimir': [],
'Volibear': [],
'Warwick': [],
'Xayah': [],
'Xerath': [],
'Xin Zhao': [],
'Yasuo': [],
'Yone': [],
'Yorick': [],
'Yuumi': [],
'Zac': [],
'Zed': [],
'Zeri': [],
'Ziggs': [],
'Zilean': [],
'Zoe': [],
'Zyra': []
}


# 이 게임 안에서 챔피언별 타임로그임
for i in range(10):
    champion_dic[champN_position.index[i]].append(champN_position.iloc[i])

print(champion_dic)

import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(100, 2)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

