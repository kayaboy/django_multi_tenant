from django.db import models
import uuid

# Create your models here.
class CompanyType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=128)


    def __str__(self):
        return self.name