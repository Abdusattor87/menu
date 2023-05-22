from django.db import models


class Category(models.Model):

    name=models.CharField("Название",max_length=50)
    image = models.ImageField(upload_to="Photos/")

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self) -> str:
        return self.name
    