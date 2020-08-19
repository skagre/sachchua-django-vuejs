from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import filters

from django.utils import timezone

from api import serializers
from api import models
from api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializers):
        serializers.save(
            updated_on=timezone.now(), 
            user_updated=self.request.user.name
        )
    
    def get_queryset(self):
        orderbyDate = self.request.query_params.get('orderbyDate')
        if orderbyDate and orderbyDate == 'asc':
            queryset = models.Category.objects.all().order_by('created_on')
        else: 
            queryset = models.Category.objects.all().order_by('-created_on')

        return queryset


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BookSerializer  
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_update(self, serializers):
        serializers.save(
            updated_on=timezone.now(), 
            user_updated=self.request.user.name
        )

    def get_queryset(self):
        orderbyDate = self.request.query_params.get('orderbyDate')
        if orderbyDate and orderbyDate == 'asc':
            queryset = models.Book.objects.all().order_by('created_on')
        else: 
            queryset = models.Book.objects.all().order_by('-created_on')

        return queryset
    

class UserCheckLoginViewSet(ObtainAuthToken):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
        

    def post(self, request, *args, **kwargs):
        return Response({
            'id': request.user.id,
            'email': request.user.email,
            'name': request.user.name,
            'created_on': request.user.created_on
        })


