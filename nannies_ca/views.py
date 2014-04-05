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
	title = "Find a Nanny, No Finder's Fee - San Diego, CA | Nannies CA"
	description = "Nannies CA provides full-time nanny services for families in or around San Diego, CA who want a trustworthy nanny for their child or children."
	return render(request, 'index.html', {'title': title, 'description': description})


def about(request):
	title = "Safe and Trustworthy Nannies - San Diego, CA | Nannies CA"
	description = "Find a nanny with no finder's fee in San Diego, La Jolla, Coronado, Carlsbad, Oceanside, Encinitas, Solana Beach, Del Mar, or surrounding areas."
	return render(request, 'about.html', {'title': title, 'description': description})


def faq(request):
	title = "Questions About Our Nannies - San Diego, CA | Nannies CA"
	description = "Your resource for finding a safe, reliable, and trustworthy nanny to care for your child."
	return render(request, 'faq.html', {'title': title, 'description': description})


def contact(request):
	title = "Contact Us to Find a Nanny - San Diego, CA | Nannies CA"
	description = "Contact Nannies CA if you have a question about finding a San Diego nanny or if you would like to get your search started today."
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
			return render(request, 'contact.html', {'form': form, 'successful': successful, 'title': title, 'description': description})
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form, 'successful': successful, 'title': title, 'description': description})


def contact_email(request, first, last, phone, body):
	return render(request, 'contact.html')
	# return first


def blog(request):
	title = "Children's Events and Activites - San Diego, CA | Nannies CA"
	description = "San Diego children's events and activities."
	return render(request, 'blog.html', {'title': title, 'description': description})


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
	contact = forms.BooleanField(label='Please Contact Me', required=False, initial=True)
	message = forms.CharField(widget=forms.Textarea)