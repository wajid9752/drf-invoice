from rest_framework import serializers
from .models import Invoice , InvoiceDetail






class InvoiceDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = InvoiceDetail
        fields = ['id','description', 'quantity', 'unit_price','price']




class InvoiceSerializer(serializers.ModelSerializer):
    invoices = InvoiceDetailSerializer(many=True)
    class Meta:
        model = Invoice
        fields = ['id','date', 'customer_name', 'invoices']

    def create(self, validated_data):
        invoices_data = validated_data.pop('invoices')
        invoice_id = Invoice.objects.create(**validated_data)
        for invoice_data in invoices_data:
            InvoiceDetail.objects.create(invoice_id=invoice_id, **invoice_data)
        return invoice_id
    
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        invoices = validated_data.get('invoices')

        for item in invoices:
            item_id = item.get('id', None)
            if item_id:
                inv_item = InvoiceDetail.objects.get(id=item_id, invoice_id=instance)
                
                inv_item.description = item.get('description', inv_item.description)
                inv_item.quantity = item.get('quantity', inv_item.quantity)
                inv_item.unit_price = item.get('unit_price', inv_item.unit_price)
                inv_item.price = item.get('price', inv_item.price)
                
                inv_item.save()
            else:
                InvoiceDetail.objects.create(invoice_id=instance, **item)

        return instance

