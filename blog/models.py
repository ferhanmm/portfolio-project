from django.db import models
from datetime import date

# Create your models here.
#title
#pub_date
#body
#image

# create a blog models

# add the blog app to the settings

# create a migration

# migrate

# add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/')