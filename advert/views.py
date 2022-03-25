from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Ads, Rubric

from .forms import AdsForm

# Create your views here.
def index(request):
    ads = Ads.objects.all()
    rubrics = Rubric.objects.all()
    context = {'ads': ads, 'rubrics': rubrics}
    return render(request, 'advert/index.html', context)

def by_rubric(request, rubric_id):
    ads = Ads.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'ads': ads, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'advert/by_rubric.html', context)

class AdsCreateView(CreateView):
    template_name = 'show.html'
    form_class = AdsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

