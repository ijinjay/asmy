# coding=utf-8
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response #for address that is absolute
from django.core.context_processors import csrf #for Certification

from django.contrib.auth import * #for Certification
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect

from django.template import Template, Context
from django.template.loader import get_template
import datetime

from django.http import Http404

from mytest.models import *

import datetime

# test function
def hello(request):
	return HttpResponse("To Beautiful you~\n<center>JinJay</center>\n<button id=\"bt\" onclick=\"dianji()\">press</button>")

# index of app
def index(request):
	# c is used for certification
	c={}
	c.update(csrf(request))
	return render_to_response('index.html',c,context_instance=RequestContext(request))
# login function
@csrf_exempt
def my_view(request):
	try:
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if request.POST.has_key("login"):
	    	if user is not None:
	        	login(request, user)
	        	return render_to_response('cashier.html',{"isCertification":1},context_instance=RequestContext(request))
	    	else:
	        	try:
	        		user = Vip.objects.get(user_ID = username)
	        		if password == user.phone:
	        			Designers = Designer.objects.filter(isRest=True)
	        			Records = Record.objects.filter(user_ID = user)
	        			return render_to_response('customer.html',{'isCertificated':1,'Records':Records,'user':user,'Designers':Designers},context_instance=RequestContext(request))
	        	except Exception, e:
	        		try:
	        			designer = Designer.objects.get(designer_ID = username)
	        			if password == designer.phone:
	        				print 'here is it'
	        				return designer_record(request)
	        		except Exception, e:
	        			return render_to_response("error.html",{},context_instance=RequestContext(request))
	    if request.POST.has_key("zhuce"):
	    	try:
	    		from django.contrib.auth.models import User
	    		user = User.objects.create_user(username=username,password=password)
	    		user.save()
	    	except Exception, e:
	    		raise Http404
	    	return render_to_response('index.html',{},context_instance=RequestContext(request))    
	except Exception, e:
		return HttpResponse(u'<center><p style="font-size: 40px;">你无权访问!帐号或密码错误!</p></center>')
	return HttpResponse(u'<center><p style="font-size: 40px;">你无权访问!帐号或密码错误!</p></center>')
# logout function
def logout_view(request):
	# if 'q' in request.POST and request.POST['q']:
	# 	q = request.POST['q']
	# 	authors = Author.objects.all()
	# 	return render_to_response('query.html',{'authors': authors, 'query': q})
	# else:
	# 	return HttpResponse('Please submit a search term.')
	if request.POST.has_key('logout'):
		logout(request)
		return HttpResponse("logout")
	# return HttpResponse("GoodBye~")

@csrf_exempt
def query(request):
	if not request.POST.has_key('user_id'):
		return HttpResponse('Error')
	q = request.POST['user_id']
	try:
		vip_user = Vip.objects.get(user_ID = q)
		return render_to_response('result.html',{'vip_user':vip_user})
	except Exception, e:
		return HttpResponse("No Vip matched your search")



def designer_record(request):
	try:
		designer_ID = request.POST['username']
		designer = Designer.objects.get(designer_ID=designer_ID)
		now = datetime.datetime.now()
		i = 1
		result = []
		result_day=[]
		while i<now.day:
			money = 0
			records = Record.objects.extra(where=["date>=%s and date <%s and designer_ID_id = %s"],params=[str(now.year)+'-'+str(now.month)+'-'+str(i),str(now.year)+'-'+str(now.month)+'-'+str(i+1),designer_ID])
			for r in records:
				money += r.money
			result.append(int(money))
			result_day.append([now.year,now.month,i])
			i += 1
		Records = Record.objects.extra(where=["date>=%s and designer_ID_id=%s"],params=[str(now.year)+'-'+str(now.month)+'-1',designer_ID])
		money = 0
		for x in Records:
			money += x.money
		return render_to_response('employee.html',{'result':result,'result_day':result_day,'isCertificated':1,'Records':Records,'designer':designer},context_instance=RequestContext(request))
	except Exception, e:
		return render_to_response('employee.html',{'isCertificated':0},context_instance=RequestContext(request))

@csrf_exempt
def vip_record(request):
	user_ID = request.POST['user_ID']
	user = Vip.objects.get(user_ID=user_ID)
	user_records = Record.objects.extra(where=["user_ID_id = %s"],params=[user_ID])
	isrests = Designer.objects.filter(isRest = True)
	return render_to_response("user_view.html",{'user_records':user_records,'user':user,'isrests':isrests})

# in the first day of a month change set performance of designers to zero
def performance_to_zero():
	d = Designer.objects.all()
	try:
		for x in d:
			x.performance = 0
			x.save()
	except Exception, e:
		raise e
	return true
@csrf_exempt
def regist_user_page(request):
	c={}
	c.update(csrf(request))
	return render_to_response('regist_user.html',c,context_instance=RequestContext(request))
@csrf_exempt
def regist_designer_page(request):
	c={}
	c.update(csrf(request))
	return render_to_response('regist_designer.html',c,context_instance=RequestContext(request))
@csrf_exempt
def regist_user(request):
	c={}
	c.update(csrf(request))
	try:
		try:
			user = Vip.objects.get(user_ID = request.POST['user_id'])
			return HttpResponse(u"该帐号已注册")
		except Exception, e:
			print "This id hasn't been used."+request.POST['user_id']
		try:
			balance = request.POST['balance']
		except Exception, e:
			return HttpResponse(u"金额输入错误，请正确输入!")
		user = Vip(user_ID = request.POST['user_id'],
					name = request.POST['name'],
					phone = request.POST['phone'],
					birth = request.POST['birth'],
					balance = balance)
		user.save()
		print "new user "+user.user_ID+user.name+user.balance
		return HttpResponse(u"注册成功！<br />点击查询查看余额")
	except Exception, e:
		raise e
	print 'failure'
	return HttpResponse(u"注册失败，请重新操作！")
@csrf_exempt
def regist_designer(request):
	c={}
	c.update(csrf(request))
	try:
		try:
			designer = Designer.objects.get(designer_ID = request.POST['designer_ID'])
			return HttpResponse(u"该帐号已注册")
		except Exception, e:
			print "This id hasn't been used."
		if not request.POST['designer_ID'] :
			return HttpResponse(u"请输入设计师ID~")
		designer = Designer(designer_ID = request.POST['designer_ID'],
					name = request.POST['name'],
					phone = request.POST['phone'],
					birth = request.POST['birth'],
					performance=0)
		designer.save()
		print "new designer "+designer.designer_ID+designer.name
		return HttpResponse(u"注册成功！<br />登陆以查看个人信息")
	except Exception, e:
		print 'failure'
	return HttpResponse(u"注册失败，请重新操作！")

@csrf_exempt
def vip_consume(request):
	c={}
	c.update(csrf(request))
	try:
		try:
			user = Vip.objects.get(user_ID = request.POST['user_id'])
		except Exception, e:
			return HttpResponse(u"会员ID错误!")
		try:
			designer = Designer.objects.get(designer_ID = request.POST['designer_ID'])
		except Exception, e:
			return HttpResponse(u"设计师ID错误！请重新输入!")
		money = request.POST['money']
		try:
			money = int(money)
		except Exception, e:
			return HttpResponse(u"金额输入错误，请正确输入!")
		if  (money>user.balance):
			return HttpResponse(u"余额不足！请充值!")
		record = Record(user_ID=user,
				designer_ID=designer,
				consume_type=request.POST['type'],
				money=money)
		record.save()
		user.balance = user.balance-money
		user.save()
		designer.performance = designer.performance + money
		print request.POST['designer_ID']+request.POST['type']+request.POST['user_id']
		print "Success vip consume"
		return HttpResponse(u"操作成功！<br />点击查询查看余额")
	except Exception, e:
		print "Vip consume failure"
		return HttpResponse(u"操作失误，请重新操作！")
@csrf_exempt
def non_vip(request):
	c={}
	c.update(csrf(request))
	try:
		user = Vip.objects.get(user_ID = '00000')
		try:
			designer = Designer.objects.get(designer_ID = request.POST['designer_ID'])
		except Exception, e:
			return HttpResponse(u"设计师ID错误！请重新输入!")
		money = request.POST['money']
		try:
			money = int(money)
		except Exception, e:
			return HttpResponse(u"金额输入错误，请正确输入!")
		record = Record(user_ID=user,
				designer_ID=designer,
				consume_type=request.POST['type'],
				money=money)
		record.save()
		print 'here'
		user.balance = user.balance-money
		user.save()
		designer.performance = designer.performance + money
		designer.save()
		print request.POST['designer_ID']+request.POST['type']+"non_vip"
		print "Success non_vip consume "+designer.designer_ID
		return HttpResponse(u"操作成功！")
	except Exception, e:
		print "Non_vip consume failure"
		return HttpResponse(u"操作失误，请重新操作！")

@csrf_exempt
def add_money(request):
	c={}
	c.update(csrf(request))
	try:
		try:
			user = Vip.objects.get(user_ID=request.POST['user_id'])
		except Exception, e:
			return HttpResponse(u"会员ID错误!")
		money = request.POST['money']
		try:
			money = int(money)
		except Exception, e:
			return HttpResponse(u"金额输入错误，请正确输入!")
		user.balance = user.balance + money;
		user.save()
		print "add_money Success "+user.user_ID	
		return HttpResponse(u"操作成功！<br />点击查询查看余额")
	except Exception, e:
		print 'add_money failure'
		return HttpResponse(u"操作失误，请重新操作！")