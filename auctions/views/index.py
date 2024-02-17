from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..forms import ListingForm
from ..models import Category, Listing, Comment

def create(request):
    if request.method == "GET":
        categories = Category.objects.all()
        form = ListingForm()
        return render(request, "auctions/create.html", {
            "categories": categories,
            "form": form
        })
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.seller = request.user
            new_list.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            categories = Category.objects.all()
            return render(request, "auctions/create.html", {
                "categories": categories,
                "form": form
            })

def NewComment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    user = request.user
    comment = request.POST.get('text', '')
    newComment = Comment(
        user = user,
        listing = listing,
        text = comment,
    )
    newComment.save()
    return HttpResponseRedirect(reverse("list",args=(listing_id, )))