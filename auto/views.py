from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Auto, CarReview, Brand
from .serializers import AutoSerializer , RegisterSerializer, LoginSerializer, CarReviewSerializer, BrandSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import  SearchFilter, OrderingFilter



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


@api_view(['POST'])
def logout(request):
    
    if request.user.is_authenticated:
        Token.objects.filter(
            user=request.user
        ).delete()
        return Response({
            'message': "Logout successful"
        })
    return Response({
        'message': " не был авторизован"
    })


@api_view(['POST'])
def login(request):
  
    serializer = LoginSerializer(
        data=request.data
    )
    if serializer.is_valid():
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(
            user = user
        )
        return Response({
            'messages': "Login successful",
            'token': token.key
        })
    return Response(
        serializer.errors,
        status=400
    )



@api_view(['POST'])
def register(request):

    serializer = RegisterSerializer(
        data=request.data
    )
    if serializer.is_valid():
        user = serializer.save()

        return Response(
            {
                "Answer": "Successfull",
                'username': user.username
            },
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )




class AutoListCreateView(ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title','type_car' ]
    search_fields = ['description','title']



class AutoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer



class CarReviewListCreateView(ListCreateAPIView):
    serializer_class = CarReviewSerializer

    def get_queryset(self):
        queryset = CarReview.objects.all()

        min_rating = self.request.query_params.get('min_rating')

        if min_rating:
            queryset = queryset.filter(raiting__gte=min_rating)

        return queryset




class CarReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarReview.objects.all()
    serializer_class = CarReviewSerializer



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer




# @api_view(['GET'])
# def auto_list(request):
#     auto = Auto.objects.all()
#     paginator = PageNumberPagination()
#     paginator.page_size = 1
#     page = paginator.paginate_queryset(auto, request)
#     serializers = AutoSerializer(page, many = True)
#     return paginator.get_paginated_response(serializers.data)
    

# @api_view(['POST'])
# def auto_create(request):
#     serializers = AutoSerializer(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data)
        
#     return Response(serializers.errors)


# @api_view(['PUT','PATCH'])
# def auto_update(request, pk):
#     auto = Auto.objects.get(pk = pk)
#     serializers = AutoSerializer(
#         auto,
#         partial = True,
#         data=request.data
#         )
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data)
#     return Response(serializers.errors)


# @api_view(['GET'])
# def auto_detail(request, pk):
#     auto = Auto.objects.get(pk = pk)
#     serializers = AutoSerializer(auto)
#     return Response(serializers.data)
    

# @api_view(['DELETE'])
# def auto_delete(request, pk):
#     auto = Auto.objects.get(pk = pk)
#     auto.delete()
#     return Response({
#         "mesages": "The car was deleted"
#     })
    

