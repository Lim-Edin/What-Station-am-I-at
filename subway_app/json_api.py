# from .models import Subway
import urllib.parse
import requests
# from . import views

main_api = 'http://swopenapi.seoul.go.kr/api/subway/4d766f5757766c6634324e716e6245/json/realtimePosition/0/100/'


subwayNm = urllib.parse.quote_plus(str(input("몇 호선? ")))

# if subwayNm == 'quit' or subwayNm == 'q':
# break

try:
    url = main_api + subwayNm
    print(url)
except Exception as ex:
    print('다시 입력해주세요!', ex)

json_data = requests.get(url).json()

try:
    json_total = json_data['errorMessage']['total']
    print('운행하고 있는 열차의 수 : ', json_total)
except Exception as ex:
    json_total = json_data['total']
    print('운행하고 있는 열차의 수 : ', json_total, ex)

try:
    json_status = json_data['errorMessage']['status']
    print('API status : ', json_status)
except Exception as ex:
    print('에러발생', ex)
    json_status = json_data['status']
    print('API status : ', json_status)

if json_total == 0:
    print("해당 호선에 운행하는 지하철이 없습니다 :)")

if json_status == 200:
    search_trainNm = input("몇 번 열차인가요?")
    print("입력받은 열차 번호 : ", search_trainNm)
    exist = 0
    rowNum = 0
    for each in json_data['realtimePositionList']:
        print(each['trainNo'])
        if each['trainNo'] == search_trainNm:
            rowNum = each['rowNum']
            exist = 1
            break
    if exist == 0:
        print("해당 열차가 존재하지 않습니다")
    if exist == 1:
        search_statnTnm = json_data['realtimePositionList'][rowNum]['statnTnm']
        search_statnNm = json_data['realtimePositionList'][rowNum]['statnNm']
        search_trainSttus = json_data['realtimePositionList'][rowNum]['trainSttus']
        # Subway.objects.create(TrainNo=search_trainNm, TrainSttus=search_trainSttus, StationNm=search_statnNm, StatnTnm=search_statnTnm)
        print(search_statnTnm + "행, " + search_statnNm + "역에서 ")

        if search_trainSttus == "0":
            print("진입중 입니다.")
        elif search_trainSttus == "1":
            print("도착했습니다.")
        else:
            print("출발, 이동했습니다.")


