from django.shortcuts import render
from .models import Certificate, Member


# Create your views here.
def index(request):
    return render(request,"index.html")

def get_certificate(request):
    if request.method == 'POST':
        certid = request.POST['number']
        # try:
        #     details = Certificate.objects.get(cert_id=certid)
        #     context = {'details' : details}
        #     return render(request, "success.html", context)
        # except Certificate.DoesNotExist:
        #     details = Member.objects.get(certificate_num=certid)
        #     context = {'details' : details, 'member': True}
        #     return render(request, "success.html", context)
        # except Member.DoesNotExist:
        #     return render(request, "error.html")
        try:
            details = Member.objects.get(certificate_num=certid)
            context = {'details' : details, 'member': True}
            return render(request, "success.html", context)
        except Member.DoesNotExist:
            return render(request, "error.html")
