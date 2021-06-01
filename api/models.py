from django.db import models


class Case(models.Model):
    case_id = models.IntegerField(blank=True, null=True)
    case_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'case'


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    toward = models.TextField(blank=True, null=True)
    unit_price = models.IntegerField(blank=True, null=True)
    building_area = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    decoration = models.TextField(blank=True, null=True)
    floor = models.TextField(blank=True, null=True)
    unit_type = models.TextField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'house'


class HouseCase(models.Model):
    house = models.ForeignKey(House, models.DO_NOTHING, blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'house_case'


class Intermediary(models.Model):
    house_id = models.IntegerField(blank=True, null=True)
    intermediary_name = models.TextField(blank=True, null=True)
    phone = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'intermediary'


class LocationOfHouse(models.Model):
    house_id = models.IntegerField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    community_name = models.TextField(blank=True, null=True)
    part_area = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'location_of_house'


class User(models.Model):
    uid = models.AutoField(db_column='UID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', unique=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=30)  # Field name made lowercase.
    register_time = models.DateField(db_column='REGISTER_TIME')  # Field name made lowercase.
    is_admin = models.IntegerField(db_column='admin', default=0)

    class Meta:
        managed = True
        db_table = 'user'

# Create your models here.
