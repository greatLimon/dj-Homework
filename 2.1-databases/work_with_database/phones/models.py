from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length= 256)
    price = models.FloatField(max_length=128)
    image = models.CharField(max_length=256)
    release_data = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=256,unique= True)

    def __str__(self):
        return f'{self.name}'