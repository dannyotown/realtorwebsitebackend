from django.db import models

# Create your models here.


class House(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    street_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    price = models.IntegerField()
    amount_of_beds = models.IntegerField()
    amount_of_baths = models.IntegerField()
    square_feet = models.IntegerField()
