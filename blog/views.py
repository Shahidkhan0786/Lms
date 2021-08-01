from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from blog.models import post,Catagory
from django.http import HttpResponse
# Create your views here.


def home(request):

    dataa = post.acceptpost.all().order_by('-post_id')
    # datar = post.acceptpost.filter().order_by('-post_id')[0:3]
    cat = Catagory.objects.all()

    paginator = Paginator(dataa, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    d = {'data': page_obj,  'catag': cat}
    return render(request , 'blog/index.html',d)


def postDetail(request,slug):
    data=post.objects.get(slug=slug)
    cat = Catagory.objects.all()
    d = {'data': data, 'catag': cat}
    return render(request , 'blog/blogdetail.html' ,d)




def search(request):
    if request.method == "POST":
        datas = request.POST['query']
        data1 = post.objects.filter(title__icontains=datas)
        data2 = post.objects.filter(author__username__contains=datas)
        data3 = post.objects.filter(content__icontains=datas)
        data = data1.union(data2, data3)
        if data.count == 0:
            messages.warning(request, "no result can be found please refine your query")

    d = {'data': data}
    return render(request, 'blog/search.html', d)


def CatagoryWise(request , catagory):
    print(catagory)
    data=post.objects.filter(catagory= catagory)
    cat = Catagory.objects.all()
    d={'data':data ,'catag':cat}
    return render(request , 'blog/index.html', d)



