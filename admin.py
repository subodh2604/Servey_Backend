from django.contrib import admin
from .models import question_answer,test,saved_test

# Register your models here.
admin.site.register(question_answer)
admin.site.register(test)
admin.site.register(saved_test)