import pandas as pd
import json


#csv 불러오기인데 이거 말고 아래껄로 해서 해야할 듯 함
data = pd.read_csv("timeline/KR_6561085084.csv")


with open('timeline/KR_6561085084.json', 'r') as f:
    data = json.load(f)


df = pd.DataFrame(data)

print('-'*80)
# print(df.iloc[0])
# print(df.iloc[1])
# print(df.iloc[2])
# print(df.iloc[2]['metadata'])
# print(df.iloc[2]['info']) #참가자 정보
# print(df.iloc[3])
# print(df.iloc[4]) #timeline
# print(df.iloc[4]['info'])
# print(df.iloc[5])

info = df.iloc[4]['info']
# for i in info:
#     info_keys = i.keys()
#     print(info_keys)


# print(info[0]['events'])
# print(info[0]['participantFrames'])
# print(info[0]['timestamp'])

# for i in info:
#     print(type(i['events']))

# part_df = pd.DataFrame(info[0]['participantFrames'])
# print(part_df)
# print(type(info[0]))

print('-'*88)
print('-'*88)
print('-'*88)
# info[1]
# print(info[1]['events'])
events_info = pd.DataFrame(info[1]['events'])
# print(events_info)
# print(type(info[1]['events']))
# print(len(info[1]['events']))
# print(info[1]['participantFrames'])
# print(info[1]['timestamp'])

# for i in info[1]['events']:
#     print(type(i))

# print(info[1]['events'][0]) # 아래 줄과 같은 내용임
# print(df.iloc[4]['info'][1]['events'][0])

# print(df.iloc[4]['info'][1]['events'][2])

# for i in range(20):
#     print(df.iloc[4]['info'][1]['events'][i])

# for i in range(21, 80):
#     print(df.iloc[4]['info'][1]['events'][i])

# info[2]
# print(len(info[2]['events']))


for i in range(len(info[2]['events'])):
    if info[2]['events'][i].get('type') in ['ITEM_UNDO', 'ITEM_PURCHASED', 'ITEM_DESTROYED', 'SKILL_LEVEL_UP', 'LEVEL_UP']:
        pass
    else:
        print(i)
        # print('-'*10, i, '-'*10)
        # print(info[2]['events'][i])

#정리
