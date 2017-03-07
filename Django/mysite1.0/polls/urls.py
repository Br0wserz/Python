from django.conf.urls import url
from . import views

urlpatterns = [
    #/polls/
    url(r'^$', views.index, name ='index'),
    #/polls/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),
]

