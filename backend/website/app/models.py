from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Localility(models.Model):
    name = models.CharField(max_length=256)


class LocalilityUser(models.Model):
    kwargs = dict(on_delete=models.CASCADE, related_name='locality')
    locality = models.ForeignKey(Localility, **kwargs)
    kwargs = dict(on_delete=models.CASCADE, related_name='proposition')
    user = models.ForeignKey(User, **kwargs)

    class Meta:
        unique_together = [['user', 'locality']]


class Proposition(models.Model):
    kwargs = dict(on_delete=models.CASCADE, related_name='propositions')
    locality = models.ForeignKey(Localility, **kwargs)
    external = models.BooleanField(default=False)
    title = models.CharField(max_length=252)
    addition_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    description = models.TextField()


class Vote(models.Model):
    kwargs = dict(on_delete=models.CASCADE, related_name='votes')
    proposition = models.ForeignKey(Proposition, **kwargs)
    in_favor = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    kwargs = dict(on_delete=models.CASCADE, related_name='comments')
    proposition = models.ForeignKey(Proposition, **kwargs)
    kwargs = dict(on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    addition_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey("self", **kwargs)
    text = models.TextField()

