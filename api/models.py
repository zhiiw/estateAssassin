from django.db import models


class House(models.Model):
    price_unit=models.IntegerField(db_column='')
    price_sum=models.IntegerField()
    area_size = models

class agent(models.Model):


class position(models.Model):


class seller(models.Model):


class case(models.Model):

class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', unique=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=30)  # Field name made lowercase.
    register_time = models.DateField(db_column='REGISTER_TIME')  # Field name made lowercase.
    role = models.IntegerField(db_column='ROLE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'


# Create your models here.
