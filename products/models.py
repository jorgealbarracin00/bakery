from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Materials(models.Model):
    materials = models.CharField(max_length=100)
    mat_mod_date = models.DateTimeField('date modified')


class Supplier(models.Model):
    def __str__(self):
        return self.name_sup

    BAK_PROD = 'Bakery Products'
    FRESH_VEG = 'Fresh Vegetables'
    FRUITS = 'Fruits'
    PACKAGING = 'Packaging'
    PASTRY_PROD = 'Pastry Products'
    CLEANING = 'Cleaning Products'
    SERVICES = 'Services'
    KITCHEN_PROD = 'Kitchen Products'

    AREAS = [
        (BAK_PROD, 'Bakery Products'),
        (FRESH_VEG, 'Fresh Vegetables'),
        (FRUITS, 'Fuits'),
        (PACKAGING, 'Packaging Material'),
        (PASTRY_PROD, 'Pastry Products'),
        (CLEANING, 'Cleaning Products'),
        (SERVICES, 'Services'),
        (KITCHEN_PROD, 'Kitchen Products')
    ]

    name_sup = models.CharField(max_length=30)
    area = models.CharField(
        max_length=80,
        choices=AREAS,
        null=True
    )
    address = models.CharField(max_length=100)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    off_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, blank=True)
    mob_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, blank=True)
    email = models.EmailField(max_length=100, null=True)


class Brand(models.Model):
    def __str__(self):
        return self.brandname
    brandname = models.CharField(max_length=100, null=True, blank=True)


class Ingredient(models.Model):
    def __str__(self):
        return self.ingredient

    PIECE = 'Piece'
    KG = "Kilogram"
    LITRE = 'Litre'
    BOX = 'Box'
    BAG1K = '1 Kg Bag'
    BAG15K = '15 Kg Bag'
    BAG20K = '20 Kg Bag'
    BOTTLE1L = '1 Lt Bottle'
    BOTTLE4L = '4 Lt Bottle'
    BOTTLE5L = '5 Lt Bottle'
    BUCKET4L = '4 Lt Bucket'
    BUCKET20L = '20 Lt Bucket'

    UNIT = [
        (PIECE, 'Pieces'),
        (KG, 'Kilograms'),
        (LITRE, 'Litre'),
        (BOX, 'Box'),
        (BAG1K, '1 Kg Bag'),
        (BAG15K, '15 Kg Bag'),
        (BAG20K, '20 Kg Bag'),
        (BOTTLE1L, '1 Lt Bottle'),
        (BOTTLE4L, '4 Lt Bottle'),
        (BOTTLE5L, '5 Lt Bottle'),
        (BUCKET4L, '4 Lt Bucket'),
        (BUCKET20L, '20 Lt Bucket')
    ]

    ingredient = models.CharField(max_length=80)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    ing_mod_date = models.DateField(null=True, blank=True)
    unit = models.CharField(max_length=20, choices=UNIT, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True)


class Unit(models.Model):
    unit = models.CharField(max_length=5)
    main_unit = models.CharField(max_length=5)
    # calc_unit =
