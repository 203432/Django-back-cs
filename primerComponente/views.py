from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importaciones de modelos 
from primerComponente.models import PrimerTabla

# Importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer

# Importacion para poder parsear a JSON
import json


# Create your views here.





class PrimerTablaList(APIView):
    def createJson(self,message,data,status):
        custom={"messages":message,"pay_load":data,"status":status}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk


    def get(self, request, format=None):
        queryset=PrimerTabla.objects.all()
        serializer=PrimerTablaSerializer(queryset,many=True ,context={'request':request})
        responseOk=self.createJson("succes",serializer.data, status =status.HTTP_200_OK)
        return Response(responseOk)

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

 

class PrimerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = PrimerTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos deja checo como te arreglo mi pana",status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = PrimerTablaSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Eliminao",  status = status.HTTP_200_OK)
        else:
            return Response("Dato no econtrado", status = status.HTTP_400_BAD_REQUEST)

