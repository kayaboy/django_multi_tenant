from django.shortcuts import render
import qrcode
import segno
from segno import helpers
import qrcode.image.svg
from io import BytesIO

def index(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "qr.html", context)

