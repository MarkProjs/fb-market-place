from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    message = models.TextField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return f'from {self.sender}: {self.message[:20]}... --> {self.receiver}'
