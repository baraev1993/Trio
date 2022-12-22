from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=70)
    def str(self):
        return self.title


class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    poster = models.ImageField(upload_to='film', null=True)
    runtime = models.IntegerField()
    cast = models.TextField()
    category =models.ForeignKey(Category, related_name='film', on_delete=models.CASCADE)
