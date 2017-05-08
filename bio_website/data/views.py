from django.shortcuts import render
import json,csv,os
# Create your views here.
from django.http import HttpResponse
from data.models import *
from django import forms
from django.template import Context,loader
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def Navi(request):
	
	if request.user.is_authenticated():
		if request.user.username=='root1':
			username=request.user.username
			context={'username':username,'tem_name':'data/root-tem.html'}
			
		else:
			username=request.user.username
			context={'username':username,'tem_name':'data/user-tem.html'}
			
	else:
		context = {'username':'','tem_name':'data/visitor-tem.html'}

	return context
	


def success(request):
	context = Navi(request)
	from_page = request.META.get('HTTP_REFERER', '/') 
	
	context['from_page'] = from_page
	return render(request,'data/success.html',context)

def database(request):
	context = Navi(request)
		
	return render(request,'data/database.html',context)

@login_required(login_url='/login')
def input(request):
	if request.method == 'POST':
		getgenedata = GetGeneData(request.POST,request.FILES)
		
		if getgenedata.is_valid():
	
			data = GeneData()

			data.GeneStandardName = getgenedata.cleaned_data['GeneStandardName']
			data.SystematicID = getgenedata.cleaned_data['SystematicID']
			data.Synonyms = getgenedata.cleaned_data['Synonyms']
			data.Product = getgenedata.cleaned_data['Product']
			data.ProductSize = getgenedata.cleaned_data['ProductSize']
			data.Pic_1 = getgenedata.cleaned_data['Pic_1']
			data.Pic_2 = getgenedata.cleaned_data['Pic_2']
			data.Pic_3 = getgenedata.cleaned_data['Pic_3']
			data.Pic_4 = getgenedata.cleaned_data['Pic_4']
			data.Pic_1text = getgenedata.cleaned_data['Pic_1text']
			data.Pic_2text = getgenedata.cleaned_data['Pic_2text']
			data.Pic_3text = getgenedata.cleaned_data['Pic_3text']
			data.Pic_4text = getgenedata.cleaned_data['Pic_4text']
			Mitolist = getgenedata.cleaned_data['MitoFeature']
			Microlist = getgenedata.cleaned_data['MicroFeature']
			Celllist = getgenedata.cleaned_data['CellFeature']

			data.save()

			Mitolist = Mitolist.split(',')
			Mitolist.pop(0)
			Mitolist = list(set(Mitolist))
			for mito in Mitolist:
				MitoFeature = Mitochondria()
				MitoFeature.FeatureName = mito
				MitoFeature.save()
				MitoFeature.SystematicIDs.add(data)

			Microlist = Microlist.split(',')
			Microlist.pop(0)
			Microlist = list(set(Microlist))
			for micro in Microlist:
				MicroFeature = Microtubule()
				MicroFeature.FeatureName = micro
				MicroFeature.save()
				MicroFeature.SystematicIDs.add(data)


			Celllist = Celllist.split(',')
			Celllist.pop(0)
			Celllist = list(set(Celllist))
			for cell in Celllist:
				
				CellFeature = Cell()
				CellFeature.FeatureName = cell
				CellFeature.save()
				CellFeature.SystematicIDs.add(data)
		
			return redirect('/success')
		else:
			return redirect('/fail')
	else:
		return redirect('/fail')

@login_required(login_url='/login')
def addtag(request):
	if request.method == "POST":
		tag = Tag(request.POST)
		if tag.is_valid():
			tagname = tag.cleaned_data["TagName"]
			featurename = tag.cleaned_data["FeatureName"]
			feature_list = eval("%s.objects.all()"%tagname)
			if featurename not in feature_list:
				newtag = eval("%s()"%tagname)
				newtag.FeatureName = featurename
				newtag.save()
				return redirect('/success')
	return redirect('/fail')


def result(request,ID):
	context = Navi(request)
	genedata = GeneData.objects.get(SystematicID=ID)
	feature_list_mito = genedata.mitochondria_set.all()
	feature_list_micro = genedata.microtubule_set.all()
	feature_list_cell = genedata.cell_set.all()
	
	context['GeneData'] = genedata
	context['feature_list_mito'] = feature_list_mito
	context['feature_list_micro'] = feature_list_micro
	context['feature_list_cell'] = feature_list_cell
	
	
	return render(request,'data/result.html',context)




def login(request):
	context = Navi(request)
	if not request.user.is_authenticated():
		return render(request,'data/login.html',context)
	else:
		return redirect('/')

def mainpage(request):
	context = Navi(request)
		
	return render(request,'data/mainpage.html',context)


def loginmid(request):
	if request.method == "POST":
		login_infor = login_f(request.POST)
		if login_infor.is_valid():
			username = login_infor.cleaned_data['username']
			password = login_infor.cleaned_data['password'] 
			user=auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				
				auth.login(request, user)
				return redirect('/user')
			
	return redirect('/fail')

def fail(request):
	context = Navi(request)
	from_page = request.META.get('HTTP_REFERER', '/') 
	
	context['from_page'] = from_page
	return render(request,'data/fail.html',context)


@login_required(login_url='/login')
def user(request):
	context = Navi(request)	
	return render(request,'data/user.html',context)

@login_required(login_url='/login')
def logout(request):

	user=request.user
	auth.logout(request)
	return redirect('/')

@login_required(login_url='/login')
def change_password(request):
	context = Navi(request)
	return render(request,'data/change-password.html',context)

@login_required(login_url='/login')
def change_password_mid(request):
	if request.method == "POST":
		change_infor = change_f(request.POST)
		if change_infor.is_valid():
			oldpassword = change_infor.cleaned_data['oldpassword']
			newpassword = change_infor.cleaned_data['newpassword'] 
			username=request.user.username
			user=auth.authenticate(username=username,password=oldpassword)
			if user is not None and user.is_active:
				
				user.set_password(newpassword)
				return redirect('/')
			
				
				
	return redirect('/fail')
		

@login_required(login_url='/login')
def usermanage(request):
	context = Navi(request)
	username=request.user.username	
	if not username=='root1':
		return redirect('/fail')
	else:
		
		return render(request,'data/usermanage.html',context)

@login_required(login_url='/login')
def addmid(request):
	username=request.user.username
	if username=='root1':
			
		add_infor=add_f(request.POST)
		if add_infor.is_valid():
				username=add_infor.cleaned_data['username']
				password=add_infor.cleaned_data['password']
				user=User.objects.filter(username__exact=username)
				if not user:
					User.objects.create_user(username,'',password)
					
					return redirect('/usermanage')
	return redirect('/fail')

@login_required(login_url='/login')
def getdata(request):
		username=request.user.username
		if not username=='root1':
			return redirect('/fail')
		else:
			ulist=User.objects.filter() 
			response_data={"rows":[]}
			deletestr1='<form action="../delete/'
			deletestr2='"><input type="submit" class="btn btn-default" value="delete"></input></form>'
			for user in ulist:
				response_data["rows"].append({"name":user.username,"delete":deletestr1+user.username+deletestr2})
				
			
		return HttpResponse(json.dumps(response_data))

@login_required(login_url='/login')
def user_delete(request,username):
		user=request.user.username
		if not user=='root1':
			return redirect('/fail')
		else:
			user=User.objects.get(username=username) 
			user.delete()
			
			return redirect('/usermanage')

@login_required(login_url='/login')
def list_all(request,feature):
	if request.method == 'GET':
		all_list = eval("%s.objects.all()"%feature)
		ret_list = list(map(lambda x:x.FeatureName,all_list))
		return HttpResponse(json.dumps(ret_list))
	return redirect('/fail')

@login_required(login_url='/login')
def ajax(request):
	if request.method == 'GET':
		ID = request.GET['ID']
		GeneStandardName=''
		Synonyms='Name Description'
		Product=''
		ProductSize=''
		
		with open("./data/static/data/file/PeptideStats.tsv") as f_1:
			reader = csv.reader(f_1,delimiter='\t')
			for row in reader:
				if row[0]==ID:
					Ps_2=row[1]
					Ps_1=row[4]
		with open("./data/static/data/file/gene_association.pombase") as f_2:
			reader = csv.reader(filter(lambda row: row[0]!='!', f_2),delimiter='\t')
			for row in reader:
				if row[1]==ID:
					GeneStandardName=row[2]
					Product=row[9]
				
		Ps_1=Ps_1+'aa,'
		Ps_2 = '%.2f'%(float(Ps_2)/1000)+'kDa'	
		ProductSize=Ps_1+Ps_2
		data={\
		'GeneStandardName':GeneStandardName,\
		'Synonyms':'Name Description',\
		'Product':Product,\
		'ProductSize':ProductSize\
		}
		return HttpResponse(json.dumps(data))
	return redirect('/fail')

def search_name(request):
	if request.method == 'GET':
		search_list = []
		if not 'SystematicID' in request.GET.keys():
			GeneStandardName = request.GET['GeneStandardName']
			search_list =  GeneData.objects.filter(GeneStandardName__iregex = r'%s'%GeneStandardName)
		if not 'GeneStandardName' in request.GET.keys():
			SystematicID = request.GET['SystematicID']
			search_list = GeneData.objects.filter(SystematicID__iregex = r'%s'%SystematicID)

		context = Navi(request)
		context['search_list'] = search_list
		if search_list == []:
			return redirect('/fail')
		return render(request,'data/result_search.html',context)
	else:
		return redirect('/fail')

def search_feature(request):
	if request.method == 'GET':

		Mitolist = request.GET['MitoFeature']
		Microlist = request.GET['MicroFeature']
		Celllist = request.GET['CellFeature']

		Mitolist = Mitolist.split(',')
		Mitolist.pop(0)
		Mitolist = list(set(Mitolist))
		query = GeneData.objects.filter()
		if Mitolist != ['default']:
			for mito in Mitolist:
				query = list(set(query)&set(Mitochondria.objects.get(FeatureName = mito).SystematicIDs.all()))

		Microlist = Microlist.split(',')
		Microlist.pop(0)
		Microlist = list(set(Microlist))
		if Microlist != ['default']:
			for micro in Microlist:
				query = list(set(query)&set(Microtubule.objects.get(FeatureName = micro).SystematicIDs.all()))

		Celllist = Celllist.split(',')
		Celllist.pop(0)
		Celllist = list(set(Celllist))
		if Celllist != ['default']:
			for cell in Celllist:
				query = list(set(query)&set(Cell.objects.get(FeatureName = cell).SystematicIDs.all()))
		
		context = Navi(request)
		context['search_list'] = query
		if query == []:
			return redirect('/fail')
		return render(request,'data/result_search.html',context)
	else:
		return redirect('/fail')

@login_required(login_url='/login')
def data_delete(request):
	
	user=request.user.username
	if not user=='root1':
		return redirect('/fail')
	else:
		if request.method == 'GET':
			SystematicID = request.GET['SystematicID']
			data = GeneData.objects.get(SystematicID = SystematicID)

			data.Pic_1.delete()
			data.Pic_2.delete()
			data.Pic_3.delete()
			data.Pic_4.delete()
			data.delete()

			return redirect('/success')
	return redirect('fail')


@login_required(login_url='/login')
def tag_delete(request):
	
	user=request.user.username
	if not user=='root1':
		return redirect('/fail')
	else:
		if request.method == 'GET':
			TagName = request.GET['TagName']
			FeatureName = eval("request.GET['%s']"%TagName)
			Tag = eval("%s.objects.get(FeatureName = FeatureName)"%TagName)


			Tag.delete()

			return redirect('/success')
	return redirect('fail')


