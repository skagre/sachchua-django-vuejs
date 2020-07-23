from rest_framework import serializers

from api import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class BookSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='user.name')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = models.Book
        fields = ('id', 'url', 'title', 'author', 'thumbnail', 'category', 'category_name', 'user', 'created_by', 'created_on', 'updated_on', 'user_updated')
        read_only_fields = ('id', 'created_by', 'created_on', 'category_name')


class CategorySerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='user.name')
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'user', 'created_by', 'created_on', 'updated_on', 'user_updated', 'books')
        read_only_fields = ('id', 'created_by', 'created_on')




