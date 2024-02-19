from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def default_category(cls):
        return cls.objects.get(name='Other')

class Listing(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='listing_images', null=True, blank=True, default="no-image.jpg")
    description = models.CharField(max_length=350)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=Category.default_category, related_name="category")
    price = models.IntegerField()
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="winner")
    seller= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="seller")
    is_active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    sold = models.TextField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    text = models.CharField(max_length=180)

    def __str__(self):
        return f"{self.user}: comment in {self.listing}"

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="requests")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True, related_name="requests")
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}: request in {self.listing}"

class Notification(models.Model):
    STATUS_CHOICES = (
        ('Normal', 'Normal'),
        ('Success', 'Success'),
        ('Danger', 'Danger'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Normal')
    reference_number = models.IntegerField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        created_at_formatted = self.created_at.astimezone(timezone.get_current_timezone()).strftime("%d-%m-%Y %H:%M")
        return f"{self.user} '{created_at_formatted}' : {self.message}"

@receiver(post_save, sender=Listing)
def create_notification(sender, instance, created, **kwargs):
    if not created and not instance.is_active:
        if instance.winner:
            message = f"Your request for listing '{instance.name}' has been accepted."           
            Notification.objects.create(
                user=instance.winner, 
                message=message, 
                reference_number=instance.id, 
                status='Success'
            )
            other_requests = Request.objects.filter(listing=instance).exclude(user=instance.winner)
            for request in other_requests:
                message = f"Your request for listing '{instance.name}' has not been accepted."
                Notification.objects.create(
                    user=request.user,
                    message=message,
                    reference_number=instance.id,
                    status='Danger'
                )
        else:
            requests = Request.objects.filter(listing=instance)
            for request in requests:
                message = f"Your request for listing '{instance.name}' has not been accepted."
                Notification.objects.create(
                    user=request.user,
                    message=message,
                    reference_number=instance.id,
                    status='Danger'
                )