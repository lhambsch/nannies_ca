from django.db import models
from django.contrib.auth.models import User

class Nanny(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address1 = models.CharField(max_length=100, null=True)
	address2 = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=50, null=True)
	state = models.CharField(max_length=20, null=True)
	zip = models.CharField(max_length=14, null=True)
	phone1 = models.CharField(max_length=14, null=True)
	phone2 = models.CharField(max_length=14, null=True)
	phone3 = models.CharField(max_length=14, null=True)
	email = models.EmailField(max_length=254, null=True)
	weekly_pay = models.FloatField(null=True)
	user = models.ForeignKey(User, related_name="nanny_user", null=True)

class Family(models.Model):
	mother_first_name = models.CharField(max_length=50, null=True)
	mother_last_name = models.CharField(max_length=50, null=True)
	father_first_name = models.CharField(max_length=50, null=True)
	father_last_name = models.CharField(max_length=50, null=True)
	address1 = models.CharField(max_length=100, null=True)
	address2 = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=50, null=True)
	state = models.CharField(max_length=20, null=True)
	zip = models.CharField(max_length=14, null=True)
	phone1 = models.CharField(max_length=14, null=True)
	phone2 = models.CharField(max_length=14, null=True)
	phone3 = models.CharField(max_length=14, null=True)
	email = models.EmailField(max_length=254, null=True)
	full_time_children = models.IntegerField()
	part_time_children = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	start_date = models.DateField(null=True)
	monthly_charge = models.FloatField(null=True)
	nanny = models.ForeignKey(Nanny, related_name="family_nanny", null=True)
	user = models.ForeignKey(User, related_name="family_user", null=True)

class Article(models.Model):
	article = models.TextField()
	author = models.ForeignKey(User, related_name="blog_author", null=True)
	created_on = models.DateField(auto_now_add=True)
	title = models.CharField(max_length=70)

	class Meta:
		ordering = ['-created_on']


	def __unicode__(self):
		return u'{0}'.format(self.title)



class Comment(models.Model):
	author = models.ForeignKey(User, related_name="comment_author")
	comment = models.TextField()
	created_on = models.DateField(auto_now_add=True)
	article = models.ForeignKey(Article, related_name="comment_blog", null=True)
