from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework_bulk import ListBulkCreateUpdateAPIView

from bulk_load.models import Answer
from bulk_load.serializers import UserSerializer, GroupSerializer, AnswerSerializer


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


# https://github.com/miki725/django-rest-framework-bulk/issues/30


#the view
class AnswerList(ListBulkCreateUpdateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
