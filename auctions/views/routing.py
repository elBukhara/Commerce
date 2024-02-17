from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

from ..models import *
from .index import *

def landing(request):
    return render(request, "auctions/landing.html")

def index(request):
    listings = Listing.objects.filter(is_active=True).order_by("-id")
    return render(request, "auctions/index.html", {
        "listings": listings
    })

def listing(request, listing_id):
    try:
        listing = get_object_or_404(Listing, pk=listing_id)
        context = {"listing": listing}
        
        if request.user == listing.seller:
            return render(request, "auctions/test.html", context)
        return render(request, "auctions/listing.html", context)
    
    except Http404:
        return render(request, "auctions/error/404.html")


def profile(request):
    user = request.user
    requests = user.requests.all().count()
    won = user.winner.all().count()
    listings = Listing.objects.filter(seller=user).order_by("-id")

    context = {
        "listings": listings,
        "requests": requests,
        "won": won
    }

    return render(request, "auctions/profile.html", context)

def allCategory(request):
    allcategory = Category.objects.all()
    return render(request, "auctions/allcategories.html", {
        "categories": allcategory
    })

def category(request, category_id):
    chosenCategory = Category.objects.get(pk=category_id) #defines what category is clicked 
    category = Category.objects.get(name = chosenCategory) #retrieves the chosen category from Category class
    categoryListings = Listing.objects.filter(is_active=True, category=category) #displays all listings within the category
    return render(request, "auctions/category.html", {
        "categories": categoryListings,
        "name": chosenCategory
    })

def allwatchlist(request):
    currentuser = request.user
    listings = currentuser.watchlist.all() #gets all watchlist from the user
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })