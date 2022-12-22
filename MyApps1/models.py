from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse;
#Create your models here....
class Employee(models.Model):
    empno=models.IntegerField();
    ename=models.CharField(max_length=128)
    job=models.CharField(max_length=128)
    sal=models.IntegerField()
    def get_absolute_url(self):
        def __str__(self):
            return self.ename
        return reverse('detail',kwargs={'pk':self.pk})

from django.db import models
#Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
