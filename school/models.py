from django.db import models


# Create your models here.


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    ggirlnum = models.IntegerField()
    ggirlnum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname


class Student(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sgender = models.BooleanField()
    scontend = models.CharField(max_length=30)
    # 外键
    sgrade = models.ForeignKey("Grades", on_delete=models.SET_NULL, null=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.sname
