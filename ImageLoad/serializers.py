from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from ImageLoad.models import TablaArchivo

class TablaArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaArchivo
        fields = ('pk','name_img','format_img', 'url_img')