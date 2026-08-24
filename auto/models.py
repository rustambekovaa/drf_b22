from django.db import models



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

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.title

    
# car = {
#     'title':"BMW",
    
# }

# MODEL
# serializer 
# JSON 

