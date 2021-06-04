from rest_framework import serializers
from comments.models import Comment
from .models import Picture


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('phone', 'email', 'comment')
        model = Comment


class PictureSerialiser(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        fields = '__all__'
        model = Picture

    def get_image_url(self, obj):
        return obj.image.url
