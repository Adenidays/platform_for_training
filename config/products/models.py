
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_data = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.pk}-{self.title}'


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.title


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.name
