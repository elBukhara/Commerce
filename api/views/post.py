from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from auctions.models import Listing, User, Request
from rest_framework.generics import get_object_or_404
from ..serializers import RequestSerializer

@api_view(['GET'])
def postWatchlist(request, pk):
    listing = Listing.objects.get(id=pk)
    user = request.user

    if user in listing.watchlist.all():
        listing.watchlist.remove(user)
        message = "Listing was removed from the watchlists"
    else:
        listing.watchlist.add(user)
        message = "Listing was added to the watchlists"

    return Response({'message': message})

@api_view(['GET'])
def postRequest(request, pk):
    listing = Listing.objects.get(id=pk)
    user = request.user 

    if request.user in listing.requests.all():

        listing.requests.remove(user)
        message = "Your Request was REMOVED"

    else:

        listing.requests.add(user)
        message = "Your Request was SUCCESSFULL"

    return Response({'message': message})

class RequestCreateView(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, request_id):
        request_obj = get_object_or_404(Request, id=request_id)
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def closeListing(request, pk, reason, winner):
    listing = Listing.objects.get(id = pk)
    listing.is_active = False

    if reason == "otherPlace":
        listing.sold = "In other place"
    elif reason == "other":
        listing.sold = "For another reason"
    else:
        listing.sold = reason
        listing.winner = User.objects.get(pk=winner)
        
    listing.save()

    message = f"listing was closed, reason: {reason}"
    
    return Response({'message': message})