from django.db import models
# Create your models here.

FILESIZE_CHOICES = (
	("500MB","500MB"),
	("1GB","1GB"),
	("3GB","3GB"),
	("5GB","5GB"),
)

class InputForm(models.Model):
	EnterPoints=models.CharField(max_length=5,
					choices=FILESIZE_CHOICES, 
					default="Choose File Size")
	EnterQuerySize=models.IntegerField()	
	
	#NumberOfSplotFiles=models.IntegerField()
	def __unicode__(self):
		return self.datetime().sorted()