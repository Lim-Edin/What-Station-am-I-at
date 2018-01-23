from django.shortcuts import render
# from django.utils import timezone
from .models import Subway
# from rest_framework.response import Response


def subway(request):
    # posts = Posting.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'subway_app/subway.html', {'Subway': Subway})


def select(request):
    return render(request, 'subway_app/select.html')