from django.shortcuts import render

from news.models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        "newses": news,
    }
    return render(request,'news/index.html',context)

def singleview(request,pk):
    news = News.objects.get(id = pk)
    context = {
        "news": news,
    }
    return render(request,'news/singleview.html',context)
def singlcategoryview(request):
    category_name = request.GET.get('category')
    my_data = News.objects.filter(category__slug = category_name)
    context = {
        "newses": my_data,
    }
    print(my_data)
    
    return render(request,'news/index.html',context)