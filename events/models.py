from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    date = models.DateField
    time = models.TimeField
    time_span = models.TimeField
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    hosts = models.ManyToManyField(User)
    type = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    content = models.TextField
    discount_coupons = models.ForeignKey(Discount)
    is_active = models.BooleanField



