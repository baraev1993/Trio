from rest_framework.serializers import ModelSerializer
from main.models import Category, Film
from review.serializers import CommentSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
    
    def to_representation(self, instance : Film):
        rep = super().to_representation(instance)
        rep['category']= CategorySerializer(instance.category).data
        rep['comments']= CommentSerializer(instance.comments.all(), many=True).data
        # rep['rating'] = instance.average_rating
        # rep['images'] = FilmSerializer(instance.images.all(),many=True, context=self.context).data
        rep['likes']= instance.likes.count()
        
        return rep