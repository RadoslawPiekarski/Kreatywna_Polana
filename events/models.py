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


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    ROLES = (
        ('A', 'Admin'),
        ('U', 'User'),
        ('I', 'Instructor'),
    )
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    description = models.TextField
    role = models.CharField(max_length=1, choices=ROLES)

    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.full_name}"


class Kid(models.Model):
    kid_name = models.CharField(max_length=20)
    birth_date = models.DateField
    parent = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kid_name}"       # dodać Kid.user (parent_name)


class DiscountCoupons(models.Model):
    coupon_code = models.CharField(max_length=20)
    discount_high = models.IntegerField
    start_date = models.DateField
    end_date = models.DateField

    def __str__(self):
        return f"{self.start_date} / {self.end_date} {self.discount_high}"


class Event(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    date = models.DateField
    time = models.TimeField
    time_span = models.TimeField
    image = models.CharField(max_length=100, null=True)
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    instructor = models.ManyToManyField(User)
    type = models.CharField(max_length=50)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    kids = models.ManyToManyField(Kid)
    excerpt = models.CharField(max_length=200)
    content = models.TextField
    discount_coupons = models.ManyToManyField(DiscountCoupons)
    is_active = models.BooleanField

    def __str__(self):
        return f"{self.title} {self.group} {self.date} {self.time}"


class Payment(models.Model):
    kid = models.ForeignKey(Kid, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    is_paid = models.BooleanField
    date = models.DateField
    price = models.DecimalField(max_digits=6, decimal_places=2)
    coupon = models.ForeignKey(DiscountCoupons, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event} {self.kid} {self.price} {self.is_paid}"
