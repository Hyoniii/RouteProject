from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30, unique=False)
    email = models.CharField(max_length=50, unique=True)

    nickname = models.CharField(max_length=20, unique=True)
    profile_image = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name + " - " + self.email


class UserRouteLike(models.Model):
    user = models.ForeignKey(User, related_name='users',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='posts',
                             on_delete=models.CASCADE)


class UserRouteScrap(models.Model):
    user = models.ForeignKey(User, related_name='users',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='posts',
                             on_delete=models.CASCADE)
