from django.urls import path
from . import views


urlpatterns = [
    # (URL raiz)/ view dessa URL/ nome, pois se mudar a url raiz o nome vai continuar o mesmo e n vai dar conflito
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
]

