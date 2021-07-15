from django.db import models
import uuid
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    full_name = models.CharField(max_length=250)
    relationship = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
          return self.full_name
          
    def save(self, *args, **kwargs):
        user_id =  "http://abc.localhost:8000/contact/profile/" + str(self.id)
        qrcode_img = qrcode.make(user_id)
        canvas = Image.new('RGB',(500, 500), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.full_name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
