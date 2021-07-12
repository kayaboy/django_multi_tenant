from shared_app.models import CompanyType
from django.contrib import admin


# Register your models here.
@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)