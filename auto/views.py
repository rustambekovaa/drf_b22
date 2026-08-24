from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Auto
from .serializers import AutoSerializer
from rest_framework.pagination import PageNumberPagination


# @api_view(['GET','POST'])
# def auto_list(request):
#     if request.method == 'GET':
#         auto = Auto.objects.all()
#         serialisers = AutoSerializer(auto, many = True)
#         return Response(serialisers.data)

#     if request.method == 'POST':
#         serialisers = AutoSerializer(data = request.data)
#         if serialisers.is_valid():
#             serialisers.save()
#             return Response(serialisers.data)
#         return Response(serialisers.errors)



@api_view(['GET'])
def auto_list(request):
    auto = Auto.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 1
    page = paginator.paginate_queryset(auto, request)
    serializers = AutoSerializer(page, many = True)
    return paginator.get_paginated_response(serializers.data)
    


@api_view(['POST'])
def auto_create(request):
    serializers = AutoSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
        
    return Response(serializers.errors)

@api_view(['PUT','PATCH'])
def auto_update(request, pk):
    auto = Auto.objects.get(pk = pk)
    serializers = AutoSerializer(
        auto,
        partial = True,
        data=request.data
        )
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)



@api_view(['GET'])
def auto_detail(request, pk):
    auto = Auto.objects.get(pk = pk)
    serializers = AutoSerializer(auto)
    return Response(serializers.data)
    

@api_view(['DELETE'])
def auto_delete(request, pk):
    auto = Auto.objects.get(pk = pk)
    auto.delete()
    return Response({
        "mesages": "The car was deleted"
    })
    
