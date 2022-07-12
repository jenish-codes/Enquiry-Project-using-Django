from django.shortcuts import render, redirect
from .models import Enquiry


def enquiryForm(request):
    if request.method == 'POST':
        # name = request.POST.get['name']
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name,email,phone,message)
        enquiry = Enquiry.objects.create(name=name,email= email,phone=phone,message=message)
        enquiry.save()
    return render(request, "enquiry_app/enquiry.html")

def enquiryDetails(request):
    enquiry = Enquiry.objects.all()

    return render(request, "enquiry_app/enquiries_list.html", {'enquiries':enquiry})

def delete(request, id):
    enquiry = Enquiry.objects.get(id=id)
    enquiry.delete()
    return redirect('enquries')

def update(request, id):
    enquiry = Enquiry.objects.get(id=id)
    return render(request, "enquiry_app/update.html", {'e':enquiry})

def updateRecord(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    enquiry = Enquiry.objects.get(id=id)
    
    enquiry.name = name
    enquiry.email = email
    enquiry.phone = phone
    enquiry.message = message
    enquiry.save()
    return redirect('enquries')