"""Music apps models"""

from django.db import models


class Artist(models.Model):
    """Artist model"""
    name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Album(models.Model):
    """Album model"""
    name = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Song(models.Model):
    """Song model"""
    title = models.CharField(max_length=255)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    class Meta:
        ordering = ['title', ]

    def __str__(self):
        return self.title
