
from django.urls import path, include
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('recording/', views.recording, name='recording'),
    path('sign/', views.sign, name='sign'),
    path('accounts/', include('django.contrib.auth.urls')),
]
