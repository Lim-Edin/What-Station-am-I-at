from django.db import models
from django.utils import timezone

#DB에 저장해야할 이유는 없는데.. 모델을 만들어봄.
class Subway(models.Model):
    TrainNo = models.IntegerField() #열차번호
    TrainSttus = models.IntegerField() #열차상태구분. 0:진입 1:도착 외:출발
    StationNm = models.CharField(max_length=10) #역명
    StatnTnm = models.CharField(max_length=10) #종착지하철역명

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
