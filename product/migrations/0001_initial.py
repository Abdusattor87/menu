# Generated by Django 4.2.1 on 2023-06-10 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('compound', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Блюдо')),
                ('image', models.ImageField(upload_to='Photos/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, max_length=10, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.category', verbose_name='Категория')),
                ('compound', models.ManyToManyField(related_name='compounds', to='compound.compound', verbose_name='Состав')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ['name'],
            },
        ),
    ]
