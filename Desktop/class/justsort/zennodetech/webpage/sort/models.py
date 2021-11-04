from django.db import models

# Create your models here.
class Item(models.Model):
    alphaval=models.CharField(
        max_length=150,
        verbose_name='Alphabet'
    )
    integerval=models.CharField(
        max_length=150,
        verbose_name='Integer'
    )
    alphanumval=models.CharField(
        max_length=150,
        verbose_name='Alpha numeral'
    )
