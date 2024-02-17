from django.contrib import admin
from .models import User, Category, Listing, Comment, Request

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "seller", "category", "price", "winner")


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment)
admin.site.register(Request)