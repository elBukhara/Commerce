from django.contrib import admin
from .models import User, Category, Listing, Comment, Request, Notification

# Register your models here.
def set_listings_default(modeladmin, request, queryset):
    # Iterate over the selected listings
    for listing in queryset:
        # Delete the winner and requests related to the listing
        requests = Request.objects.filter(listing=listing)
        notifications = Notification.objects.filter(message__icontains=listing.name)

        # Set is_active to True
        listing.is_active = True
        listing.sold = ''

        # Delete winner and requests
        if listing.winner:
            listing.winner = None

        listing.save()
        requests.delete()

        # Delete notifications
        notifications.delete()

    # Display a success message in the admin panel
    modeladmin.message_user(request, "Selected listings have been marked as active and related data has been deleted.")

    # Set the description for the custom admin action
    set_listings_default.short_description = "Set listings to default and delete related data"

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "seller", "category", "price", "winner")
    actions = [set_listings_default]


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment)
admin.site.register(Request)
admin.site.register(Notification)