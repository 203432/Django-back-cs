from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from Profile.models import TablaProfile

class TablaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaProfile
        fields = ('__all__')