from django.db import models
from management.models import Type, Device, Location


# Create your models here.
class Review(models.Model):
    type = models.ForeignKey(Type, null=True, blank=True)
    device = models.ForeignKey(Device, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    order_by = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)
    speed_limit = models.BooleanField(default=False)
    wrong_path = models.BooleanField(default=False)
    rider_dismount = models.BooleanField(default=False)
    weaving = models.BooleanField(default=False)
    no_light = models.BooleanField(default=False)
    no_light = models.BooleanField(default=False)
    near_misses = models.BooleanField(default=False)

    def __str__(self):
        return self.location

    class Meta:
        db_table = 'reviews'
