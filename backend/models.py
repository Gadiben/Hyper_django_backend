from backend.service.auth_user_service import UserAsync

from django.db import models


class FanartType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'fanart_type'


class Platforms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'platforms'

class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'media'


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    publish_time = models.DateTimeField()
    text_content = models.CharField(max_length=300, blank=True, null=True)
    media_url = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('AppUser', models.DO_NOTHING)
    fanart = models.ForeignKey(FanartType, models.DO_NOTHING)
    media = models.ForeignKey(Media, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post'


class AppUser(models.Model):
    id = models.IntegerField(primary_key=True)
    pseudo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    longitude = models.DecimalField(max_digits=4, decimal_places=2)
    date_of_birth = models.DateField()
    latitude = models.DecimalField(max_digits=4, decimal_places=2)
    gender = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'appuser'


class UserLibrairy(models.Model):
    id = models.IntegerField(primary_key=True)
    media = models.ForeignKey(Media, models.DO_NOTHING)
    user = models.ForeignKey(AppUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_librairy'

class Tvshow(models.Model):
    id = models.ForeignKey(Media, models.DO_NOTHING, db_column='id', primary_key=True)
    season_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tvshow'

class VideoGame(models.Model):
    id = models.ForeignKey(Media, models.DO_NOTHING, db_column='id', primary_key=True)
    platform = models.ForeignKey(Platforms, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'video_game'

class Film(models.Model):
    id = models.ForeignKey(Media, models.DO_NOTHING, db_column='id', primary_key=True)
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'

class UserUserAuthDjango(models.Model):
    user_id = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)
    auth_id = models.OneToOneField(UserAsync, on_delete=models.CASCADE)
