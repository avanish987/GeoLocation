# from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    created_dtm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="place"
        verbose_name="Place"
