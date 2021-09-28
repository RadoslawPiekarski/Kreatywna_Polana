from django.contrib import admin
from .models import Place, User, Kid, Group, DiscountCoupons, Event, Payment

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_filter = ("place", "group",)
    list_display = ("title", "date", "place", "group")
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(User)
admin.site.register(Kid)
admin.site.register(Event, EventAdmin)
admin.site.register(DiscountCoupons)
admin.site.register(Place)
admin.site.register(Group)
admin.site.register(Payment)
