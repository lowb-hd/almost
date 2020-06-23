from django.db import models

# Create your models here.
class Pizza(models.Model):
    '''pizza的name'''
    name = models.CharField(max_length=200)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

class Topping(models.Model):
    """配料"""
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""

        return self.name[:50] + "..."