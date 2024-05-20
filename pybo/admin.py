from django.contrib import admin
from .models import Question
from .models import Company
from .models import Serverstatus

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)


'''
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']

admin.site.register(Company, CompanyAdmin)
'''
class ServerstatusAdmin(admin.ModelAdmin):
    search_fields = ['no']

admin.site.register(Serverstatus, ServerstatusAdmin)


# Register your models here.
