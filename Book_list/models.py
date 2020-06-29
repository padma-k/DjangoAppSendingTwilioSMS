from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    amazonlink = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
