from django.contrib import admin
from customer.models import *
# Register your models here.
admin.site.register(Customers)
admin.site.register(CustomersAddress)
admin.site.register(CustomersAadhar)