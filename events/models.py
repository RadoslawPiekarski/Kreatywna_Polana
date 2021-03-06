from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=50, null=True, blank=True, )
    place_map = models.CharField(max_length=400, null=True, blank=True)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    district = models.CharField(max_length=50, default="Osiedle Przemysława")
    city = models.CharField(max_length=20, default="Poznań")
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.street} {self.street_number}"


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class UserProfile(models.Model):
    ROLES = (
        ('A', 'Admin'),
        ('U', 'User'),
        ('I', 'Instructor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_profile')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(blank=True)
    role = models.CharField(max_length=1, choices=ROLES, default='U')

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.full_name()


class Kid(models.Model):
    kid_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kid_name}"
        # return f"{self.kid_name} Rodzic: {self.parent.first_name} {self.parent.last_name}"


class DiscountCoupons(models.Model):
    coupon_code = models.CharField(max_length=20)
    discount_high = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.coupon_code} {self.discount_high}"


class Event(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    time = models.TimeField()
    time_span = models.TimeField()
    image = models.CharField(max_length=100, null=True)
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    instructor = models.ManyToManyField(User)
    type = models.CharField(max_length=50)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    kids = models.ManyToManyField(Kid)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()
    discount_coupons = models.ManyToManyField(DiscountCoupons)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.group} {self.place} {self.date} {self.time}"


class Payment(models.Model):
    kid = models.ForeignKey(Kid, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    is_paid = models.BooleanField()
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    coupon = models.ForeignKey(DiscountCoupons, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event} {self.kid} {self.price} {self.is_paid}"
