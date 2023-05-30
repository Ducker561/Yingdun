from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=32)
    user_telephone = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_address = models.CharField(max_length=255, blank=True, null=True)
    user_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'