from rest_framework.views import APIView
from src.serializers import InvoiceSerializer
from rest_framework import generics
from .models import Invoice , InvoiceDetail
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.



class ListInvoices(APIView):
    
    def get(self, request):
        queryset = Invoice.objects.all()
        serializer = InvoiceSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {"status":"success"}
        else:
            res = {"error": str(serializer.errors)}
                
        return Response(res)
    
    def put(self , request , pk):
        obj = get_object_or_404(Invoice, pk=pk)
        data=request.data
        serializer = InvoiceSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            res = {"status":"success"}
        else:
            res = {"error": str(serializer.errors)}

        return Response(res)
    
    def patch(self , request , pk):
        obj = get_object_or_404(Invoice, pk=pk)
        data=request.data
        serializer = InvoiceSerializer(obj,data=data , partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"status":"success"}
        else:
            res = {"error": str(serializer.errors)}

        return Response(res)    
    

