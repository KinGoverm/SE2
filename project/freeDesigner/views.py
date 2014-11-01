#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#encoding:UTF-8
from django.shortcuts import render, render_to_response
from freeDesigner.forms import LoginForm
from django.template import RequestContext

def main(request):
	return render_to_response('main.html')

def login(request,redirect=0):
	if str(redirect)=="redirect":
		link = request.GET.get('next')[1:-1]
		return render_to_response('alert.html', {'error':"ابتدا باید وارد شوید",'address':'/login/'+link+'/'})
	if request.method == 'POST':

		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			
			if '@' in username :
				try:
					username = User.objects.get(email = username).username
				except:
					form.errors="لطفا ابتدا وارد لینک فعال سازی که به ایمیلتان فرستاده شده است , شوید"
					return render_to_response('login.html', {'form':form},context_instance=RequestContext(request))
				
				
			user = auth.authenticate(username=username, password=password)
			
			if user is not None and user.is_active:
				auth.login(request, user)

				
				if redirect==0:
					return HttpResponseRedirect("/controlPanel/")
				else:
					return HttpResponseRedirect("/"+redirect+"/")
					
				

			else:
				form.errors="نام کاربری یا رمز عبور اشتباه است"
				return render_to_response('login.html', {'form':form},context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form':form},context_instance=RequestContext(request))

	elif request.method == 'GET':

		form = LoginForm()
		return render_to_response('login.html', {'form':form},context_instance=RequestContext(request))
	else:
		form = LoginForm(request.POST)
		return render_to_response('login.html', {'form':form},context_instance=RequestContext(request))

