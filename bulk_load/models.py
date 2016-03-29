from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parameter(models.Model):
	name = models.CharField(max_length=100)


class Answer(models.Model):
	user = models.ForeignKey(User, null=False, blank=False)
	parameter = models.ForeignKey(Parameter, null=False, blank=False)
	answer_number = models.FloatField(null=True, blank=True)
	answer_date = models.DateField(null=True, blank=True)
	answer_boolean = models.BooleanField(default=False)
	answer_currency = models.DecimalField(null=True, blank=True, max_digits=24, decimal_places=8)

	class Meta:
		unique_together = ("user", "parameter")
