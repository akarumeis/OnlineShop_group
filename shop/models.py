from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="image/%Y/%m/%d/")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    descriprion = models.TextField()
    image = models.ImageField(upload_to="image/%Y/%m/%d/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name