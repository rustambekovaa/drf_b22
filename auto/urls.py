from django.urls import path, include
from .views import (
    # auto_list,
    # auto_create,
    # auto_detail,
    # auto_delete,
    # auto_update,
    register,
    login,
    logout,
    # CarReviewListCreateView,
    # CarReviewDetailView,
    # AutoListCreateView,
    # AutoDetailView,
    BrandViewSet,
    AutoViewSet,
    CarReviewViewSet,
    
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'brand', BrandViewSet)
router.register(r'auto', AutoViewSet)
router.register('reviews', CarReviewViewSet)

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    # path('auto/', auto_list),
    # path('auto/create/', auto_create),
    # path('auto/<int:pk>/detail/', auto_detail),
    # path('auto/<int:pk>/delete/', auto_delete),
    # path('auto/<int:pk>/update/', auto_update),
    # path('car_review/', CarReviewListCreateView.as_view()),
    # path('car_review/<int:pk>/', CarReviewDetailView.as_view()),
    # path('car/', AutoListCreateView.as_view()),
    # path('car/<int:pk>/', AutoDetailView.as_view()),
    path('', include(router.urls))
    

]