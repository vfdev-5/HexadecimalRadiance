from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField("Dataset name",unique=True, max_length=30)
    googlePlayUrl = models.URLField("Application url in Google Play Store", blank=False)
    appFile = models.FileField("Application apk file", null=False)