from django.contrib import admin
from django.urls import path
from two import views

urlpatterns = [
   path("", views.index, name='two'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("terms", views.terms, name='terms'),
   path("privacy", views.privacy, name='privacy'),
   path("faq", views.faq, name='faq'),
   path("feedback", views.feedback, name='feedbak'),
   path("complaint", views.complaint, name='complaint'),
   path("suggestion", views.suggestion, name='suggestion')
]

