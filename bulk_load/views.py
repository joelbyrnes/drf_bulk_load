from django.shortcuts import render

from rest_framework import viewsets, status
from django.contrib.auth.models import User, Group
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_bulk import ListBulkCreateUpdateAPIView
from rest_framework import mixins
from rest_framework_bulk.drf3 import mixins as bulk_mixins

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

class HackedBulkUpdateModelMixin(bulk_mixins.BulkUpdateModelMixin):
	def bulk_update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		# restrict the update to the filtered queryset
		serializer = self.get_serializer(
			self.filter_queryset(self.get_queryset()),
			data=request.data,
			many=True,
			partial=partial,
			)
		validated_data = []
		validation_errors = []
		for item in request.data:
			item_serializer = self.get_serializer(
				self.get_queryset().get(pk=item['id']),
				data=item,
				partial=partial,
				)
			item_serializer.is_valid(raise_exception=True)
			if item_serializer.errors:
				validation_errors.append(item_serializer.errors)
			validated_data.append(item_serializer.validated_data)
		if validation_errors:
			raise ValidationError(validation_errors)
		serializer._validated_data = validated_data
		self.perform_bulk_update(serializer)
		return Response(serializer.data, status=status.HTTP_200_OK)


class HackedListBulkCreateUpdateAPIView(
										# mixins.ListModelMixin,
										# bulk_mixins.BulkCreateModelMixin,
										HackedBulkUpdateModelMixin,
								  		ListBulkCreateUpdateAPIView):
	pass

#the view
class AnswerList(HackedListBulkCreateUpdateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
