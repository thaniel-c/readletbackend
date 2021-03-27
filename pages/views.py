from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pages.serializers import UserSerializer, GroupSerializer, PageSerializer
from .models import Page


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

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pages to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    #permission_classes = [permissions.IsAuthenticated]