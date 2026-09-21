from django.contrib import admin
from .models import Auto, CarReview, Brand

admin.site.register(Auto)
# admin.site.register(CarReview)
admin.site.register(Brand)


@admin.register(CarReview)
class CarReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "raiting", "user__id"]