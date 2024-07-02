from django.contrib import admin

from news.models import Category, Keyword, News,Comment

# Register your models here.
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Keyword)
admin.site.register(Category)