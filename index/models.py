from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import datetime

# Create your models here.

post_types_list=(
			('published','Published'),
			('stories','Stories'),
			('travelogue','Travelogue'),
			)

photo_types_list=(
			('people','People'),
			('nature','Nature'),
			('bnw','Black & White'),
	)

class post(models.Model):
	id=models.AutoField(primary_key=True)
	head=models.CharField(max_length=100,default="No Title")
	content=RichTextUploadingField(default="No Content")
	created_date=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_date=models.DateTimeField(auto_now_add=False,auto_now=True)
	selected_date=models.DateTimeField(default=datetime.now)
	post_type=models.CharField(max_length=20,default="published",choices=post_types_list)
	file=models.ImageField(upload_to='posts/',default='0')

	def __str__(self):
		return self.head



class photo(models.Model):
	file=models.ImageField(upload_to='uploads/')
	created_date=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_date=models.DateTimeField(auto_now_add=False,auto_now=True)
	photo_type=models.CharField(max_length=20,default="people",choices=photo_types_list)
	
	def __str__(self):
		return self.file.name

class comment(models.Model):
	name=models.CharField(max_length=20,default='Anonymous')
	email=models.CharField(max_length=30,default='anonymous')
	content=models.TextField(default='no-content')
	created_date=models.DateTimeField(auto_now_add=True,auto_now=False)
	post=models.ForeignKey(post,on_delete=models.CASCADE)

	def __str__(self):
		return self.name+" - "+self.content[0:10]

class comment_photo(models.Model):
	name=models.CharField(max_length=20,default='Anonymous')
	email=models.CharField(max_length=30,default='anonymous')
	content=models.TextField(default='no-content')
	created_date=models.DateTimeField(auto_now_add=True,auto_now=False)
	photo=models.ForeignKey(photo,on_delete=models.CASCADE)

	def __str__(self):
		return self.name+" - "+self.content[0:10]

class subscribers(models.Model):
	email=models.CharField(max_length=30,default='anonymous@gmail.com')

	def __str__(self):
		return self.email


