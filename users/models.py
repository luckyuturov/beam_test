from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь один-к-одному
    bio = models.TextField(blank=True, null=True)               # Дополнительное поле
    birth_date = models.DateField(blank=True, null=True)        # Дата рождения
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Фото

    def __str__(self):
        return self.user.username
