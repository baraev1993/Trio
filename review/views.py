from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Rating, User
from .permissions import IsAuthorOrReadOnly

from rest_framework.decorators import api_view , action 
from django.shortcuts import get_object_or_404
from main.models import Film
from .models import Favorite, LikeFilm
from main.serializers import FilmSerializer




class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        user = request.user
        ser = RatingSerializer(data=request.data, context={"request":request})
        ser.is_valid(raise_exception=True)
        film_id = request.data.get("film")
        if Rating.objects.filter(author=user, film__id=film_id).exists():
            rating = Rating.objects.get(author=user, film__id=film_id)
            rating.value = request.data.get("value")
            rating.save()
        else:
            # Rating.objects.create(user)
            ser.save()
        return Response(status=201)


@api_view(['POST'])
def favourite(request,film_id):
    if not request.user.is_authenticated:
        return Response(status=401)
    author = request.user
    # film_id =request.data.get('film')
    film = get_object_or_404(Film , id = film_id)

    if Favorite.objects.filter(film=film, author=author).exists():
        Favorite.objects.filter(film=film,author=author).delete()
    else:
        Favorite.objects.create(film=film,author=author)
    return Response(status=201)


@api_view(['POST'])
def toogle_like(request, film_id):
    # film_id = request.data.get('film')
    # author_id = request.data.get('author')
    film = get_object_or_404(Film, id=film_id)
    author = request.user
    if LikeFilm.objects.filter(film=film, author=author).exists():
        LikeFilm.objects.filter(film=film, author=author).delete()
    else:
        LikeFilm.objects.create(film=film, author=author)
    return Response(status=201)