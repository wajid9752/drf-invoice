from django.db import models



class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name +"Invoice date "+ str(self.date)
    

class InvoiceDetail(models.Model):
    invoice_id = models.ForeignKey(Invoice , on_delete=models.CASCADE , related_name="invoices")
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.invoice_id.customer_name +" Total Price "+ str(self.price)  
