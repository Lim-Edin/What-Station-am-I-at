from django.shortcuts import render
from django.utils import timezone
from .models import Posting

def subway(request):
    posts = Posting.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'subway_app/subway.html', {'posts': posts})