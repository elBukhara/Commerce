from django.urls import path

from . import views
from . import authentication

urlpatterns = [
    path("login", authentication.login_view, name="login"),
    path("logout", authentication.logout_view, name="logout"),
    path("register", authentication.register, name="register"),
    #
    path("", views.landing, name="landing"),
    path("listings", views.index, name="index"),
    path("listing/<int:listing_id>", views.listing, name="list"),
    path("watchlists", views.allwatchlist, name="allwatchlist"),
    path("category", views.allCategory, name="categories"),
    path("category/<int:category_id>", views.category , name="category"),
    path("profile", views.profile, name="profile"),
    #
    path("create", views.create, name="create"),
    path("add_Comment/<int:listing_id>", views.NewComment, name="comment"),
    #
]
