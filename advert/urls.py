from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:rubric_id>', views.by_rubric, name='by_rubric'),
    path('', views.index, name='index'),
    re_path(r'^sh', views.AdsCreateView.as_view(), name='add'),
]
