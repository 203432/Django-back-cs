from django.urls import path, re_path
from django.conf.urls import include

#Importacion de vistas
from ImageLoad.views import LoadImageTable,LoadImageTableDetail

urlpatterns = [
    re_path(r'^img/$', LoadImageTable.as_view()),
    re_path(r'^img/(?P<pk>\d+)$', LoadImageTableDetail.as_view()),
]