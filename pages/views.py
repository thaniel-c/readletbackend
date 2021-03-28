from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pages.serializers import UserSerializer, GroupSerializer, PageSerializer
from .models import Page
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PageViewSet(viewsets.ViewSet):
    """
    API endpoint that allows pages to be viewed or edited.
    """
    lookup_field = 'name'

    #https://stackoverflow.com/questions/39729388/using-django-rest-framework-to-return-info-by-name
    def list(self, request):
        queryset = Page.objects.all()
        serializer = PageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, name=None):
        queryset = Page.objects.all()
        page = get_object_or_404(queryset, name=name)
        serializer = PageSerializer(page)
        return Response(serializer.data)