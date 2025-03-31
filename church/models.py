from django.db import models
from django.contrib.auth.models import User


# Member Model
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# Sermon Model
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # Consider adding a default value or allowing null=True if it's optional
    date = models.DateField()
    video_file = models.FileField(upload_to='sermons/videos/', null=True, blank=True)
    audio_file = models.FileField(upload_to='sermons/audios/', null=True, blank=True)
    sermon_file = models.FileField(upload_to='sermons/files/', null=True, blank=True)  # For downloading
    

    def __str__(self):
        return self.title

# Give Model
class Give(models.Model):
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('mpesa', 'M-Pesa'),
        ('paypal', 'PayPal'),
        ('bank', 'Bank Transfer')
    ])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.amount}"

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # Consider adding a default value or allowing null=True if it's optional
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title   

from django.db import models

class WelcomeContent(models.Model):
    image = models.ImageField(upload_to='welcome_images/', blank=True, null=True)
    verse = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Welcome Content ({self.created_at.strftime('%Y-%m-%d')})"

