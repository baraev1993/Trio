from django.db import models
from main.models import Film
from account.models import User


class Comment(models.Model):
    film = models.ForeignKey(Film , related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    film = models.ForeignKey(Film, related_name='ratings', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

class LikeFilm(models.Model):
    author = models.ForeignKey(User,related_name='film_likes', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, related_name= 'likes',on_delete=models.CASCADE)


    
class Favorite(models.Model):
    film = models.ForeignKey(Film, related_name='favorites', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)