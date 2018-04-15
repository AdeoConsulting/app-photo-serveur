from django.conf.urls import url
from .views import PhotoList

urlpatterns = [
	url(r'^image/$', PhotoList.as_view()),
]