from django.db import models
import json

class CategoryQuerySet(models.QuerySet):
    def serialize(self):
        data = list(self.values())
        return json.dumps(data)
        
class CategoryManager(models.Manager):
    def get_queryset(self):
        return  CategoryQuerySet(self.model, using=self.db)

class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = CategoryManager()

    def serialize(self):
        return json.dumps({
            "name": self.name,
            "id": self.id
        })