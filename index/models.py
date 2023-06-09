from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_no = models.AutoField(primary_key=True)
    comment_username = models.CharField(max_length=255)
    comment_userid = models.CharField(max_length=255)
    comment_rating = models.IntegerField(blank=True, null=True)
    comment_time = models.DateTimeField()
    comment_vote = models.IntegerField()
    comment_location = models.CharField(max_length=20, blank=True, null=True)
    comment_content = models.TextField()
    comment_isspam = models.IntegerField(blank=True, null=True)
    comment_emotion=models.CharField(max_length=10, blank=True, null=True)
    movie_no = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Movie(models.Model):
    movie_no = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=255)
    movie_intro = models.TextField(blank=True, null=True)
    movie_comment1 = models.TextField(blank=True, null=True)
    movie_comment2 = models.TextField(blank=True, null=True)
    movie_score = models.CharField(max_length=5, blank=True, null=True)
    movie_director = models.CharField(max_length=255, blank=True, null=True)
    movie_writer = models.CharField(max_length=255, blank=True, null=True)
    movie_actor = models.TextField(blank=True, null=True)
    movie_genres = models.CharField(max_length=255, blank=True, null=True)
    movie_country = models.CharField(max_length=255, blank=True, null=True)
    movie_language = models.CharField(max_length=255, blank=True, null=True)
    movie_aka = models.CharField(max_length=255, blank=True, null=True)
    movie_realease = models.CharField(max_length=255, blank=True, null=True)
    movie_runtimes = models.CharField(max_length=20, blank=True, null=True)
    movie_pic = models.CharField(max_length=255, blank=True, null=True)
    movie_emotion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'

class People(models.Model):
    people_no = models.AutoField(primary_key=True)
    people_name = models.CharField(max_length=50, blank=True, null=True)
    people_signature = models.CharField(max_length=255, blank=True, null=True)
    people_locate = models.CharField(max_length=50, blank=True, null=True)
    people_nickname = models.CharField(max_length=50, blank=True, null=True)
    people_date = models.CharField(max_length=20, blank=True, null=True)
    people_ip = models.CharField(max_length=10, blank=True, null=True)
    people_pic = models.CharField(max_length=255, blank=True, null=True)
    people_nownum = models.IntegerField(blank=True, null=True)
    people_wantnum = models.IntegerField(blank=True, null=True)
    people_pastnum = models.IntegerField(blank=True, null=True)
    people_nowmovie = models.CharField(max_length=255, blank=True, null=True)
    people_pastmovie = models.CharField(max_length=255, blank=True, null=True)
    people_contacts = models.IntegerField(blank=True, null=True)
    people_revcontacts = models.IntegerField(blank=True, null=True)
    people_isspam = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'