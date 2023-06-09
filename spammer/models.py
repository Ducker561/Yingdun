from django.db import models

# Create your models here.

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