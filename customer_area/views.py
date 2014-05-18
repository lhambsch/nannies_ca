from django.shortcuts import render
from .models import Article, User, Comment, Family, Nanny

# Create your views here.
def blog(request):
	title = "Children's Events and Activites - San Diego, CA | Nannies CA"
	description = "San Diego children's events and activities."
	articles = Article.objects.all()
	return render(request, 'blog.html', {'title': title, 'description': description, 'articles': articles})


def article(request, id):
	article = Article.objects.get(pk=id)
	description = ''
	return render(request, 'article.html', {'title': article.title, 'description': description, 'article': article})