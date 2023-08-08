from sklearn.decomposition import TruncatedSVD
import pandas as pd
#그냥 실행하면 됨
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')
print('start')

# 기본 mastary data
data = pd.read_csv("mastary_2.csv")

# mastary_point.csv

# print(data) # 소환사 닉, 챔피언, 점수, ...
# df_point = data[['summonerName', 'championId', 'championPoints']]
df_point = data[['summonerName', 'championName', 'championPoints']]

# 데이터프레임을 재구조화하여 championId를 컬럼으로 만듭니다. 피벗
# df_point = data.pivot(index='summonerName', columns='championId', values='championPoints')
df_point = data.pivot(index='summonerName', columns='championName', values='championPoints')
# df_point2 = data.pivot(index='summonerName', columns='championId', values='championPoints')
df_point2 = data.pivot(index='summonerName', columns='championName', values='championPoints')
# NaN 값을 0으로 채웁니다.
df_point = df_point.fillna(0)

print(df_point)
# 저장
# df_point.to_csv('mastary_point.csv')


# mastary_level.csv
# df_level = data[['summonerName', 'championId', 'championLevel']]
df_level = data[['summonerName', 'championName', 'championLevel']]

# 데이터프레임을 재구조화하여 championId를 컬럼으로 만듭니다.
# df_level = data.pivot(index='summonerName', columns='championId', values='championLevel')
df_level = data.pivot(index='summonerName', columns='championName', values='championLevel')

# NaN 값을 0으로 채웁니다.
df_level = df_level.fillna(0)


# print(df_level.head())
#저장
# df_level.to_csv('mastary_level.csv')


# point로 SVD
svd = TruncatedSVD(n_components=25)
df_point_transformed = svd.fit_transform(df_point)
df_point_transformed = pd.DataFrame(df_point_transformed, index=df_point.index)
df_point_predicted = svd.inverse_transform(df_point_transformed)
df_point_predicted = pd.DataFrame(df_point_predicted, columns=df_point.columns, index=df_point.index)

# print(df_point_predicted.head())



# 결측값만 예측값으로 채우는 코드
df_point_fillna = df_point.copy()

# 모든 누락된 값을 예측된 값으로 채웁니다. (결측치를 아까 0으로 바꿔줘서 결측치있는 데이터프레임 다시가져옴;;;)
for champion in df_point2.columns:
    for user in df_point2.index:
        if pd.isnull(df_point2.loc[user, champion]):
            df_point_fillna.loc[user, champion] = df_point_predicted.loc[user, champion]

# 채워진 데이터프레임을 출력합니다.
# print(df_point_fillna)





# level로 SVD
svd = TruncatedSVD(n_components=25)
df_level_transformed = svd.fit_transform(df_level)
df_level_transformed = pd.DataFrame(df_level_transformed, index=df_level.index)
df_level_predicted = svd.inverse_transform(df_level_transformed)
df_level_predicted = pd.DataFrame(df_level_predicted, columns=df_point.columns, index=df_level.index)
# print(df_level_predicted.head())



# 추천 시스템
recommendations = {}

for user in df_point_fillna.index:
    # 원래의 점수와 예측 점수를 비교합니다.
    original_scores = df_point.loc[user]
    predicted_scores = df_point_fillna.loc[user]
    
    # 원래 점수가 낮은 챔피언들 중에서 예측 점수가 높은 챔피언을 찾습니다.(3명만)
    low_original_high_predicted = predicted_scores[original_scores < original_scores.median()].nlargest(3)
    
    # 해당 사용자에 대한 추천을 저장합니다.
    recommendations[user] = low_original_high_predicted.index.tolist()

# 추천 결과를 출력합니다.
print(recommendations)