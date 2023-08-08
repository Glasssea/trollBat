#match정보 가져오기
import requests


api_key = "RGAPI-78657f3e-6124-4b45-a708-104b66419301"

puuid = "HAEDMPK2OxzVOzgZx4fdKZWNsSZx-vLTgHRZTJtUJbgprUcw7aym9iXfgkaDjTCMkKMKNIRTT3HqAw"





url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/%EB%82%98%EC%81%9C%EC%9C%A0%EC%A0%80%EB%8A%94%EC%97%86%EB%8B%A4/KR1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}


response = requests.get(url, headers=headers)

print(response.json())










