from django.urls import path

from news.views import index, singleview,singlcategoryview
urlpatterns = [
    path('',index,name='index'),
    path('singleview/<int:pk>',singleview, name="singleview"),
    path('category/',singlcategoryview, name="category")
]