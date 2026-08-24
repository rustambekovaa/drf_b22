from django.urls import path

from .views import (
    auto_list,
    auto_create,
    auto_detail,
    auto_delete,
    auto_update,
)

urlpatterns = [
    path('auto/', auto_list),
    path('auto/create/', auto_create),

    path('auto/<int:pk>/detail/', auto_detail),
    path('auto/<int:pk>/delete/', auto_delete),
    path('auto/<int:pk>/update/', auto_update),
]