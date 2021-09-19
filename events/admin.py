from django.contrib import admin
from .models import Place, User, Kid, Group, DiscountCoupons, Event, Payment

# Register your models here.

admin.site.register(User)
admin.site.register(Kid)
admin.site.register(Event)
admin.site.register(DiscountCoupons)
admin.site.register(Place)
admin.site.register(Group)
admin.site.register(Payment)
