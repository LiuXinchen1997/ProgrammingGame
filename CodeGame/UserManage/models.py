# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Challengemap(models.Model):
    map_id = models.AutoField(primary_key=True)
    level = models.IntegerField()
    hint = models.TextField(blank=True, null=True)
    descr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challengemap'


class Challengemapcontent(models.Model):
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    element = models.ForeignKey('Element', models.DO_NOTHING)
    map = models.ForeignKey(Challengemap, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'challengemapcontent'


class Element(models.Model):
    element_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'element'


class Freemap(models.Model):
    map_id = models.AutoField(primary_key=True)
    hint = models.TextField(blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Userentry', models.DO_NOTHING, db_column='creator')
    createdtime = models.DateField()
    isrelease = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'freemap'


class Freemapcontent(models.Model):
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    element = models.ForeignKey(Element, models.DO_NOTHING)
    map = models.ForeignKey(Freemap, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'freemapcontent'


class Membership(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    priority = models.SmallIntegerField(blank=True, null=True)
    starttime = models.DateField()
    endtime = models.DateField()

    class Meta:
        managed = False
        db_table = 'membership'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    entry = models.ForeignKey('Userentry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user'


class Usercollect(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    map = models.ForeignKey(Freemap, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usercollect'


class Userentry(models.Model):
    username = models.CharField(unique=True, max_length=20)
    tel_number = models.CharField(unique=True, max_length=11)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'userentry'


class Userlike(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    map = models.ForeignKey(Freemap, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userlike'


class Usershare(models.Model):
    id = models.IntegerField(primary_key=True)
    map_id = models.IntegerField()
    isfree = models.IntegerField(db_column='isFree', blank=True, null=True)  # Field name made lowercase.
    solution_code = models.TextField()
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usershare'
