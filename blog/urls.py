from django.urls import path
from . import views


urlpatterns = [
    # (URL raiz)/ view dessa URL/ nome, pois se mudar a url raiz o nome vai continuar o mesmo e n vai dar conflito
    path('', views.post_list, name='post_list')
]
