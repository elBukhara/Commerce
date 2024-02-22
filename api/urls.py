from django.urls import path
from . import views
from .views import RequestCreateView

urlpatterns = [
    path('listings',  views.getListings),
    path('listings/<int:pk>',  views.getListing),
    path('user-status',  views.getUserStatus),
    path('user',  views.getUser),
    path('watchlist/<int:pk>',  views.postWatchlist),
    path('request/<int:pk>',  views.postRequest),
    path("close/<int:pk>/<str:reason>/<int:winner>", views.closeListing),
    path('make-request', RequestCreateView.as_view(), name='request-create'),
    path('delete-request/<int:request_id>', RequestCreateView.as_view()),
    path('notifications', views.getNotifications),
    path('notifications/<int:pk>/read', views.mark_notification_as_read),
]