from django.db import models


class User(models.Model):
    """User表"""

    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class Publisher(models.Model):
    """Publisher出版社"""

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name