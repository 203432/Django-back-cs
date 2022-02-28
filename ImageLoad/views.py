from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path
from pathlib import Path

# importaciones de modelos agregados
from ImageLoad.models import TablaArchivo

# importaciones de serializadores
from ImageLoad.serializers import TablaArchivoSerializer

# Create your views here.

class LoadImageTable(APIView):
    def get(self, request, format=None):
        queryset = TablaArchivo.objects.all()
        serializer = TablaArchivoSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No hay archivo para subir")
        archivos = request.data['url_img']
        #archivos = Path(request.data['name_img'])
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = TablaArchivoSerializer(data=request.data)
        # return Response({'data': str(request.data)})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            img = TablaArchivo(**validated_data)
            img.url_img =  'http://localhost:8000/assets/img/' + str(img.url_img)
            img.save()
            serializer_response = TablaArchivoSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class LoadImageTableDetail(APIView):
    def get_object(self, pk):
        try:
            return TablaArchivo.objects.get(pk = pk)
        except TablaArchivo.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = TablaArchivoSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        serializer = TablaArchivoSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        imagen = self.get_object(pk)
        if imagen != 0:
            imagen.delete()
            return Response("Dato eliminado",status=status.HTTP_204_NO_CONTENT)
        return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST) 