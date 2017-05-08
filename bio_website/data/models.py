from django.db import models
from django import forms
# Create your models here.

#数据的模型
class Tag(forms.Form):
	TagName = forms.CharField()
	FeatureName = forms.CharField()

	




class GeneData(models.Model):
	GeneStandardName = models.CharField(max_length=10)
	SystematicID = models.CharField(max_length=50,primary_key=True)
	Synonyms = models.CharField(max_length=50)
	Product = models.CharField(max_length=200)
	ProductSize = models.CharField(max_length=50)
	Pic_1 = models.ImageField()
	Pic_2 = models.ImageField()
	Pic_3 = models.ImageField()
	Pic_4 = models.ImageField()
	Pic_1text = models.CharField(max_length=50,default='Pic_1')
	Pic_2text = models.CharField(max_length=50,default='Pic_2')
	Pic_3text = models.CharField(max_length=50,default='Pic_3')
	Pic_4text = models.CharField(max_length=50,default='Pic_4')
	
	def __str__(self):
		return self.SystematicID



class GetGeneData(forms.Form):
	GeneStandardName = forms.CharField()
	SystematicID = forms.CharField()
	Synonyms = forms.CharField()
	Product = forms.CharField()
	ProductSize = forms.CharField()
	Pic_1 = forms.ImageField()
	Pic_2 = forms.ImageField()
	Pic_3 = forms.ImageField()
	Pic_4 = forms.ImageField()
	Pic_1text = forms.CharField()
	Pic_2text = forms.CharField()
	Pic_3text = forms.CharField()
	Pic_4text = forms.CharField()
	MitoFeature = forms.CharField()
	MicroFeature = forms.CharField()
	CellFeature = forms.CharField()

	def __str__(self):
		return self.SystematicID


class Mitochondria(models.Model):
	FeatureName = models.CharField(max_length=50,primary_key=True)
	SystematicIDs = models.ManyToManyField(GeneData)
	def __str__(self):
		return self.FeatureName

class Microtubule(models.Model):
	FeatureName = models.CharField(max_length=50,primary_key=True)
	SystematicIDs = models.ManyToManyField(GeneData)
	def __str__(self):
		return self.FeatureName

class Cell(models.Model):
	FeatureName = models.CharField(max_length=50,primary_key=True)
	SystematicIDs = models.ManyToManyField(GeneData) 	
	def __str__(self):
		return self.FeatureName

class login_f(forms.Form):
	username = forms.CharField()
	password = forms.CharField() 

class change_f(forms.Form):
	oldpassword=forms.CharField()
	newpassword=forms.CharField()

class add_f(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

