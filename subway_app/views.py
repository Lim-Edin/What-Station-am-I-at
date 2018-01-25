from .models import Subway
from rest_framework import generics, serializers
from rest_framework.response import Response


# 보여줄 field 명시
class SubwayListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Subway
            fields = ('id', 'title', 'TrainNo', 'TrainSttus', 'StationNm', 'StatnTnm', 'created_date')


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
