from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django import forms
from django.template import RequestContext


def home(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')


def faq(request):
	return render(request, 'faq.html')


def contact(request):
	successful = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			message = 'Name: ' + form.data['first'] + ' ' + form.data['last'] + '\nEmail: ' + form.data['email'] + '\nPhone: ' + form.data['phone'] +'\nMessage: ' + form.data['message']
			try:
				if form.data['contact']:
					message += '\nPlease contact me with more information.'
			except:
				message += '\nI would prefer that you do not contact me.'
			send_mail('Online Inquiry', message, 'noreply@nanniesca.com', ['nanniesca@gmail.com'], fail_silently=False)
			successful = True
			form = ContactForm()
			return render(request, 'contact.html', {'form': form, 'successful': successful})
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form, 'successful': successful})


def contact_email(request, first, last, phone, body):
	return render(request, 'contact.html')
	# return first


def news(request):
	return render(request, 'news.html')


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/family')
	else:
		return HttpResponseRedirect('/invalid')


def invalid(request):
	return render(request, 'invalid.html')


def family(request):
	return render(request, 'family.html')

class ContactForm(forms.Form):
	first = forms.CharField(label='First Name', max_length=20, required=False)
	last = forms.CharField(label='Last Name', max_length=20, required=False)
	phone = forms.CharField(max_length=20, required=False)
	email = forms.CharField(max_length=50, required=False)
	contact = forms.BooleanField(label='Please Contact Me', required=False)
	message = forms.CharField(widget=forms.Textarea)