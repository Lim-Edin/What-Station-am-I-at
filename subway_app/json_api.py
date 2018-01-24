from rest_framework import generics, serializers
from rest_framework.response import Response
from subway_app.models import Subway
import urllib.parse
import requests
from . import views
# from urllib.parse import urlencode, quote_plus

main_api = 'http://swopenapi.seoul.go.kr/api/subway/4d766f5757766c6634324e716e6245/json/realtimePosition/0/5/'

while True:
    subwayNm = urllib.parse.quote_plus(str(input("몇 호선? ")))

    if subwayNm == 'quit' or subwayNm == 'q':
        break

    url = main_api + subwayNm
    print(url)

    json_data = requests.get(url).json()
    json_total = json_data['total']
    print(json_total)

    try:
        json_status = json_data['errorMessage']['status']
        print(json_status)
    except Exception as ex:
        print('에러발생', ex)
        json_status = json_data['status']
        print(json_status)

    if json_total == 0:
        print("해당 호선에 운행하는 지하철이 없습니다 :)")

    if json_status == 200:
        search_trainNm = input("몇 번 열차인가요?")
        print(search_trainNm)
        exist = 0       # exist : 해당 열차번호 존재여부 bool
        for each in json_data['realtimePositionList']:
            print(each['trainNo'])
            if each == search_trainNm:
                print("지하철역명 : " + 'statnNm')
                print('trainSttus')
                exist = 1
        if exist == 0:
            print("해당 열차가 존재하지 않습니다")
