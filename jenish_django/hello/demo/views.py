from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *
from.serializers import *


@api_view(['GET'])
def gett(request):
    obj=Student.objects.all()
    serializer=studentserializer(obj, many =True)
    return Response({'status' : 200 ,'massage' : 'right','payload':serializer.data})


@api_view(['POST'])
def postt(request):
    data = request.data
    serializer = studentserializer(data = request.data)
    if not serializer.is_valid():
        return Response({'status' : 201,'massage' : 'wrong'})
    serializer.save()
    return Response({'status' : 200,'massage' : 'right','payload' : serializer.data})
                           
@api_view(['PUT'])
def putt (requst,id):
    try:
        obj=Student.object.get(id=id)
        serializer=studentserializer(obj,data=requst.data)
        if not serializer.is_valid():
            return Response({'status': 201, 'message':'WRONG'})
        serializer.save()
        return Response ({'status':200, 'massage':'RIGHT','payload': serializer.data})
    except Exception as d :
        return Response({'status':403,'massage':'ERROR'})
    
 