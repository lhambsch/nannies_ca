from django.contrib import admin

from .models import Family, Nanny, Article, Comment


admin.site.register(Family)
admin.site.register(Nanny)
admin.site.register(Article)
admin.site.register(Comment)