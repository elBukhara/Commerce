from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from auctions.models import *
from ..serializers import ListingSerializer, UserSerializer

from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
def getListing(request, pk):
    try:
        listing = Listing.objects.get(id=pk)
        listingData = ListingSerializer(instance=listing, many=False, context={'request': request}).data
        return Response(listingData)
    
    except ObjectDoesNotExist:
        context = {
            "error": "Listing not found"
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getListings(request):
    listings = Listing.objects.all().order_by("-id")
    serializer = ListingSerializer(instance=listings, many=True, context={'request': request}).data
    return Response(serializer)

@api_view(['GET'])
def getUserStatus(request):
    is_authenticated = request.user.is_authenticated
    user_profile = None

    if is_authenticated:
        user = request.user

        user_profile = {
            "id": user.id,
            "user_name": user.username,
            "date_joined": "24/12/2006"
        }
    data = {
        "is_authenticated": is_authenticated,
        "user_profile": user_profile
    }

    return Response(data)

@api_view(['GET'])
def getUser(request):

    response = {'is_active': "false"}

    try:
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response(response)