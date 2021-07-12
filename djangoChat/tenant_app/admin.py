from tenant_app.models import Company
from django.contrib import admin

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
