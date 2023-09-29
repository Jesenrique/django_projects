from django.shortcuts import render
from blogApp.models import categorie, post

# Create your views here.

def blog(request):
    posts=post.objects.all()
    return render(request, "blog/blog.html",{"posts":posts})

def blog_categorie(request, categorie_id):
    categori=categorie.objects.get(id=categorie_id)
    posts=post.objects.filter(categories=categori)
    return render(request, "blog/blog_categorie.html",{"categorie":categori, "posts":posts})
    