from django.test import TestCase, Client
from .views import ContactForm
from django.core import mail


class ContactTestCase(TestCase):
	def test_contact_inital_page_load(self):
		client = Client()
		response = client.get('/contact/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'contact.html')


	def test_contact_without_message(self):
		client = Client()
		form_data = {'first': 'test', 'last': 'test', 'phone': '123-456-7890', 'email': 'test@gmail.com', 'contact': True, 'message': ''}
		form = ContactForm(data=form_data)
		response = client.post('/contact/', form_data)
		# form = ContactForm(response.request.POST)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'contact.html')
		self.assertEqual(form.is_valid(), False)


	def test_contact_with_message(self):
		client = Client()
		form_data = {'first': 'test', 'last': 'test', 'phone': '123-456-7890', 'email': 'test@gmail.com', 'contact': True, 'message': 'test'}
		form = ContactForm(data=form_data)
		response = client.post('/contact/', form_data)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'contact.html')
		self.assertEqual(form.is_valid(), True)


	def test_send_email(self):
		mail.send_mail('Online Inquiry', 'test message', 'noreply@nanniesca.com', ['nanniesca@gmail.com'], fail_silently=False)
		self.assertEquals(len(mail.outbox), 1)
		self.assertEquals(mail.outbox[0].subject, 'Online Inquiry')
		self.assertEquals(mail.outbox[0].body, 'test message')


class HomeTestCase(TestCase):
	def test_home_page_load(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')


class AboutTestCase(TestCase):
	def test_about_page_load(self):
		client = Client()
		response = client.get('/about/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'about.html')


class FaqTestCase(TestCase):
	def test_faq_page_load(self):
		client = Client()
		response = client.get('/faq/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'faq.html')


class BlogTestCase(TestCase):
	def test_blog_page_load(self):
		client = Client()
		response = client.get('/blog/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog.html')
