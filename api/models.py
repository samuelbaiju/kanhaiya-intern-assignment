from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or str(self.telegram_id)

    