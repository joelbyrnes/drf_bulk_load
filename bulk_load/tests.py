from django.test import TestCase, Client
import django
import json

from bulk_load.models import Answer, Parameter

django.setup()

# Create your tests here.

class TestStuff(TestCase):
	def test_bulk_create(self):
		client = Client()

		data = [
			{'parameter': Parameter.objects.create(name='a').id, 'user': 1},
			{'parameter': Parameter.objects.create(name='b').id, 'user': 1},
		]

		response = client.post("/answers/", data=json.dumps(data), content_type='application/json')
		# print response.content
		results = json.loads(response.content)

		print results

	def test_bulk_update(self):
		client = Client()

		data = [
			{'parameter': Parameter.objects.create(name='a').id, 'user': 1},
			{'parameter': Parameter.objects.create(name='b').id, 'user': 1},
			]

		response = client.post("/answers/", data=json.dumps(data), content_type='application/json')
		# print response.content
		results = json.loads(response.content)

		print results

		data = [
			{'id': results[0]['id'], 'parameter': Parameter.objects.create(name='a').id, 'user': 1},
			{'id': results[1]['id'], 'parameter': Parameter.objects.create(name='b').id, 'user': 1},
			]

		response = client.patch("/answers/", data=json.dumps(data), content_type='application/json')


	def xtest_nothing(self):
		pass

