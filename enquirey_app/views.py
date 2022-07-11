from django.shortcuts import render, redirect



def enquiryForm(request):
    if request.method == 'POST':
        # name = request.POST.get['name']
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
    return render(request, "enquiry_app/enquiry.html")

# def enquiryDetails(request):
#     return render(request, template_name)