from django.contrib import admin
from .models import Place, UserProfile, Kid, Group, DiscountCoupons, Event, Payment

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_filter = ("place", "group",)
    list_display = ("title", "date", "place", "group")
    prepopulated_fields = {"slug": ["title"]}


class KidAdmin(admin.ModelAdmin):
    list_display = ("kid_name", "parent")

admin.site.register(UserProfile)
admin.site.register(Kid, KidAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(DiscountCoupons)
admin.site.register(Place)
admin.site.register(Group)
admin.site.register(Payment)
