from shared_app.models import CompanyType
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    company_type = models.ForeignKey(CompanyType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name