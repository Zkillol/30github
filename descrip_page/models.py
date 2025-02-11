from django.db import models



class Comments(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField()
    likes = models.IntegerField
    img = models.ImageField(upload_to='img/' , null=True , blank=True )

