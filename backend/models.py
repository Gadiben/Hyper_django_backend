# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FanartType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'fanart_type'


class Platforms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'platforms'


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    publish_time = models.DateTimeField()
    text_content = models.CharField(max_length=300, blank=True, null=True)
    media_url = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    fanart = models.ForeignKey(FanartType, models.DO_NOTHING)
    media = models.ForeignKey(Media, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    pseudo = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=4, decimal_places=2)
    date_of_birth = models.DateField()
    latitude = models.DecimalField(max_digits=4, decimal_places=2)
    gender = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_'


class UserLibrairy(models.Model):
    id = models.IntegerField(primary_key=True)
    media = models.ForeignKey(Media, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_librairy'

class Tvshow(models.Model):
    id = models.ForeignKey(Media, models.DO_NOTHING, db_column='id', primary_key=True)
    season_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tvshow'

class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'

class VideoGame(models.Model):
    id = models.ForeignKey(Media, models.DO_NOTHING, db_column='id', primary_key=True)
    platform = models.ForeignKey(Platforms, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'video_game'

class Film(models.Model):
    id = models.ForeignKey('Media', models.DO_NOTHING, db_column='id', primary_key=True)
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'
