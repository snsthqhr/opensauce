from django.contrib import admin
from .models import Question, Diagnosis, GPTResponse

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Diagnosis)
admin.site.register(GPTResponse)

# Register your models here.
