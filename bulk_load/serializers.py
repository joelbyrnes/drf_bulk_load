from rest_framework import serializers
from rest_framework_bulk import ListBulkCreateUpdateAPIView
from rest_framework_bulk.drf3.serializers import BulkSerializerMixin, BulkListSerializer

from django.contrib.auth.models import User, Group
from tinyobj.fields import NoValidationField
from bulk_load.models import Answer


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')


# https://github.com/miki725/django-rest-framework-bulk/issues/30

#the serializer
class AnswerSerializer(BulkSerializerMixin, serializers.ModelSerializer):
	# answer = NoValidationField()

	class Meta:
		model = Answer
		# fields = ['id', 'answer', 'parameter', 'user']
		fields = ['id', 'parameter', 'user']
		list_serializer_class = BulkListSerializer
