from rest_framework.serializers import ModelSerializer, SerializerMethodField
from auctions.models import Listing, User, Comment, Request

class ListingSerializer(ModelSerializer):
    seller_username = SerializerMethodField()
    requests = SerializerMethodField()
    comments = SerializerMethodField()
    category = SerializerMethodField()

    def get_seller_username(self, obj):
        return obj.seller.username

    def get_requests(self, obj):
        requests = obj.requests.all()
        requests = list(requests.values("user_id", "user__username", "text"))
        return requests

    def get_comments(self, obj):
        comments = obj.comments.all()
        comments = list(comments.values("user_id", 'user__username', 'text'))
        return comments

    def get_category(self, obj):
        return obj.category.name

    def to_representation(self, obj):
        data = super().to_representation(obj)
        request = self.context.get('request')
        
        if request.user.is_authenticated:
            # If the requested_user is NOT the seller, we return relavent data to the client 
            if not(request and request.user == obj.seller):

                data['is_added_watchlist'] = request.user in obj.watchlist.all()
                data['is_added_request'] = Request.objects.filter(listing=obj, user=request.user).exists()
                data['requests'] = obj.requests.all().count()
                data['watchlist'] = obj.watchlist.all().count()
                
                if data['is_added_request']:
                    text = Request.objects.filter(listing=obj, user=request.user)
                    data['requested_text'] = list(text.values("id", "text"))
            # Otherwise, if the requested_user IS the seller, outer functions above will work automatically 
        else:
            data['requests'] = obj.requests.all().count()
            data['watchlist'] = obj.watchlist.all().count()

        return data

    class Meta:
        model = Listing
        fields = ['is_active', 'category', 'description', 'id', 'image', 'name', 'price', 
                  'requests', 'seller_username', 'sold', 'watchlist', 'winner', 'comments']
        

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text']

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = ['user', 'listing', 'text']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'