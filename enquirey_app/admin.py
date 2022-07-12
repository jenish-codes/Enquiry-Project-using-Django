from django.contrib import admin
from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    fields = ['name','email','phone','message']

admin.site.register(Enquiry, EnquiryAdmin)