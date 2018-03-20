from django.db import models


# Create your models here.
class TypeGroup(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_groups'


class Type(models.Model):
    typegroup = models.ForeignKey(TypeGroup)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'types'


class Device(models.Model):
    type = models.ForeignKey(Type)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'devices'


class Location(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'locations'
