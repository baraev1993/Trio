from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=70)
    
    def __str__(self):
        return self.title


class Film(models.Model):
    genre = models.ForeignKey(Category, related_name='film', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.DateField()
    poster = models.ImageField(upload_to='film', null=True)
    runtime = models.PositiveIntegerField()
    cast = models.TextField()

