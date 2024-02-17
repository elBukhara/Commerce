from django.contrib.auth.models import AbstractUser
from django.db import models

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