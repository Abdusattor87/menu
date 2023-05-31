from django.db import models


class Compound(models.Model):

    name=models.CharField("Название",max_length=50) 

    class Meta:
        verbose_name="Состав"
        verbose_name_plural="Состав"

    def __str__(self) -> str:
        return self.name