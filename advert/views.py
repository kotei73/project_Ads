from django.shortcuts import render

from .models import Ads

# Create your views here.
def index(request):
    ads = Ads.objects.all()
    context = {'adsf': ads}
    return render(request, 'advert/index.html', context)
