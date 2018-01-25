from django.db import models
from django.utils import timezone

# DB에 저장해둘.. 소팅될 객체의 기반인 모델을 만들어봄.


class Subway(models.Model):
    title = models.CharField(max_length=200)
    TrainNo = models.IntegerField()     # 열차번호
    TrainSttus = models.IntegerField()  # 열차상태구분. 0:진입 1:도착 외:출발
    StationNm = models.CharField(max_length=10)  # 역명
    StatnTnm = models.CharField(max_length=10)  # 종착지하철역명

    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
