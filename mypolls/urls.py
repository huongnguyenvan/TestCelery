# Create new file `ce/urls.py` to define url of app ce
from django.conf.urls import url
from mypolls import views

urlpatterns = [
    url(r'^$', views.index),
]
