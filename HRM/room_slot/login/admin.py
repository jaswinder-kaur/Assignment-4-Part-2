from django.contrib import admin
from login.models import Customer
from booking.models import Contact,Rooms,Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Rooms)
admin.site.register(Booking)