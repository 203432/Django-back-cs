from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny



class RegistroView(generics.CreateAPIView):
     queryset = User.objects.all()
     permission_classes = (AllowAny,)
     serializer_class = RegisterSerializer


    # def post(self, request):
    #     serializer =  RegistroSerializer(data = request.data) 
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
# Create your views here.
