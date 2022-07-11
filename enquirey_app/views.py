from django.shortcuts import render



def enquiryForm(request):
    return render(request, 'enquiry_app/enquiry.html')