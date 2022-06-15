from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
