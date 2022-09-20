from django.db import models

from accounts.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    text = models.TextField()
    title = models.CharField(max_length=200)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)



