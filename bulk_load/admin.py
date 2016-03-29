from django.contrib import admin

# Register your models here.

from bulk_load.models import Answer, Parameter

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	pass
	# list_display = ('','')

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
	pass


