from django.shortcuts import render
# from django.utils import timezone
from .models import Subway
from rest_framework import generics, serializers
from rest_framework.response import Response


class SubwayListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Subway
            fields = ('TrainNo', 'TrainSttus', 'StationNm', 'StatnTnm')


# GET하면 이 listview로 연결
class SubwayListView(generics.ListAPIView):
    queryset = Subway.objects.all()
    serializer_class = SubwayListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)


def subway(request):
    # posts = Posting.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'subway_app/subway.html', {'Subway': Subway})


def select(request):
    return render(request, 'subway_app/select.html')