from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=50, null=True)
    place_map = models.CharField(max_length=400, null=True)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    district = models.CharField(max_length=50, default="Osiedle Przemysława")
    city = models.CharField(max_length=20, default="Poznań")

    def __str__(self):
        return f"{self.name} {self.street} {self.street_number}"

class Event(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    date = models.DateField
    time = models.TimeField
    time_span = models.TimeField
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    hosts = models.ManyToManyField(User)
    type = models.CharField(max_length=50)
    group = models.ForeignKey(Group)
    image = models.CharField(max_length=100, null=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField
    discount_coupons = models.ForeignKey(Discount, null=True)
    is_active = models.BooleanField

    def __str__(self):
        return f"{self.title} {self.group} {self.date} {self.time}"




