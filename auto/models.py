from django.db import models
from django.contrib.auth.models import User


class  Brand(models.Model):
    name = models.CharField(max_length= 150,verbose_name= ' Называние модли ')
    year = models.IntegerField()
    description = models.CharField(verbose_name = 'История')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


    def __str__(self):
        return self.name



class Auto(models.Model):

    TYPE_CHOICES = (
    ("passenger_cars","легоковые"),
    ( "cargo" ,'грузовой'),
    ("motorbike" ,"мотоцикл")
    )
    
    title = models.CharField(max_length=200, verbose_name="Называние")
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    type_car = models.CharField(choices=TYPE_CHOICES, verbose_name="Тип машины")
    year = models.IntegerField(verbose_name='Год выпуска')
    created_at = models.DateTimeField()
    brand = models.ForeignKey(
        Brand,
        on_delete = models.CASCADE,
        related_name = 'autos'
    )
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.title

    
class CarReview(models.Model):

    CAR_RAITING = (
        (1, '⭐️'),
        (2, '⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️'),
        (5, '⭐️⭐️⭐️⭐️⭐️'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review'
    )
    name = models.CharField(max_length= 200, verbose_name = "Имя")
    text = models.TextField( verbose_name = "Оценка")
    raiting = models.IntegerField(choices=CAR_RAITING,  verbose_name = "Рейтинг" )
    
    car = models.ForeignKey(
        Auto,
        on_delete = models.CASCADE,
        related_name = 'review'
    )
    created_at = models.DateTimeField(auto_now_add = True)


    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.name} - {self.car} '


 
