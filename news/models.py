from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,blank=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
class Keyword(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Comment(models.Model):
    user_name = models.CharField(max_length=20)
    comment = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user_name
    
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    comment = models.ManyToManyField(Comment,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)#category id
    keyword = models.ManyToManyField(Keyword)
    image = models.ImageField(upload_to="blogimage/")
    def __str__(self):
        return self.title