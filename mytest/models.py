from django.db import models

class Vip(models.Model):
	"""docstring for Vip"""
	user_ID = models.CharField(max_length = 10,primary_key = True)
	phone = models.CharField(max_length = 15)
	balance = models.IntegerField()
	birth = models.CharField(max_length= 20)
	name = models.CharField(max_length = 20)
	def __unicode__(self):
		return self.user_ID		

class Designer(models.Model):
	"""docstring for Designer"""
	designer_ID = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length = 20)
	phone = models.CharField(max_length = 15)
	birth = models.CharField(max_length= 20)
	isRest = models.BooleanField()
	performance = models.IntegerField()
	def __unicode__(self):
		return self.designer_ID		
		
class Record(models.Model):
	"""docstring for Record"""
	user_ID = models.ForeignKey(Vip)
	designer_ID = models.ForeignKey(Designer)
	date = models.DateTimeField(auto_now = True)
	money = models.IntegerField()
	consume_type = models.CharField(max_length = 20)
	def __unicode__(self):
		return self.money

