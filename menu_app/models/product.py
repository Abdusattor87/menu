from django.db import models

class  Product(models.Model):

    name =models.CharField("Блюдо",max_length=70,null=False) 
    category=models.ForeignKey("menu_app.category",on_delete=models.CASCADE,related_name="categories",verbose_name="Категория",null=False)
    image = models.ImageField(upload_to="Photos/")
    price =models.DecimalField("Цена",max_length=10,max_digits=6,decimal_places=2) 
    compound=models.ManyToManyField("menu_app.compound" ,related_name="compounds",verbose_name="Состав")


    class Meta:
        ordering=["name"]
        verbose_name="Блюдо"
        verbose_name_plural="Блюда"

    def __str__(self) -> str:
        return self.name
 