from django.db import models
from django.utils import timezone


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250, unique=True)
    template = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    week = models.CharField(max_length=250)
    weekday = models.CharField(max_length=250)
    shift = models.CharField(max_length=250)
    opening_hours = models.CharField(max_length=250)
    availability = models.CharField(max_length=250)

    def __str__(self):
        return self.week

    class Meta:
        ordering = ['week']

    class Admin:
        pass


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    warehouses = models.ManyToManyField(Warehouse)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass


class TruckCompany(models.Model):
    truck_company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass


class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    returned_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    returns = models.ManyToManyField(Return)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class Admin:
        pass
