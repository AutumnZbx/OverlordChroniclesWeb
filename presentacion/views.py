from django.shortcuts import render
import qrcode
from django.http import HttpResponse
from io import BytesIO


def home(request):
    user_agent = request.user_agent
    context = {
        'is_mobile': user_agent.is_mobile,
        'is_tablet': user_agent.is_tablet,
        'is_pc': user_agent.is_pc,
    }
    return render(request, 'mi_app/home.html', context)


def qr_code(request):
    apk_url = "https://github.com/AutumnZbx/OverlordChroniclesApk/raw/refs/heads/main/OverlordChronicles.apk"
    qr = qrcode.make(apk_url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")