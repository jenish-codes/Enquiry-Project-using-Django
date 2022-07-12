from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiryForm, name="enquiryForm" ),
    path('enquries/', views.enquiryDetails, name="enquries"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    path('update-enquiry/<int:id>', views.updateRecord, name="update-enquiry"),
]