from django.db import models

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""

        return self.text[:50] + "..."

class UserInfo(models.Model):
    user_id = models.CharField("user id ",max_length=4,primary_key=True)
    user_name = models.CharField("user name",max_length=10)
    password = models.CharField("password",max_length=10)
    status = models.CharField("user status 有效/无效",default=1,max_length=5)