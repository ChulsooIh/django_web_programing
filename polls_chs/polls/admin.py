from django.contrib import admin
from .models import *

#class

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]



# Register your models here.
admin.site.register(Question, QuestionAdmin)
