from django.db import models
import os



# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=50,default="Enter your file name")
    upload_date=models.DateTimeField(auto_now=True)
    extension=models.CharField(max_length=50,default="pdf")
    path = models.FileField(upload_to='uploads/',verbose_name="select file")
    size = models.FloatField("filesize",default=0.0)
   

    def __str__(self) -> str:
        return self.name




class Download(models.Model):

    file = models.ForeignKey(File, verbose_name="file name", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    last_download = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file



