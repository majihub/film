from django.http import HttpResponse
from django.shortcuts import render, redirect

from . forms import movieform
from . models import movie

# Create your views here.
def index(request):
    obj=movie.objects.all()
    context={
        'movie_list':obj
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    obj=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':obj})
def addmovie(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        direc = request.POST.get('director')
        img = request.FILES['img']
        add = movie(name=name,desc=desc,year=year,director=direc,img=img)
        add.save()
    return  render(request,'add.html')
def update(request,id):
    obj=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':obj})
def delete(request, id):
    if request.method=='POST':
        obj=movie.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
