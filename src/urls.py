from django.urls import path 
from .views import ListInvoices
urlpatterns = [
    
    path('invoices-list/' , ListInvoices.as_view() ),
    path('invoices-list/<int:pk>/' , ListInvoices.as_view() ),
]
