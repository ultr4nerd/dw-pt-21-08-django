"""Movies app models"""

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    release_date = models.DateField()
    stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    sinopsis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['title', 'director']

    def __str__(self):
        return self.title
