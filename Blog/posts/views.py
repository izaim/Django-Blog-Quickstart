from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_create(request): #create post
    return HttpResponse("<h1>Create</h1>")

def post_detail(request): #read post
    context = {
        "title": "Detail"
    }
    return render(request,"index.html", context)
    #return HttpResponse("<h1>Detail</h1>")

def post_list(request): #list posts
    if request.user.is_authenticated():
        context ={
            "title": "List"
        }
    else:
        context ={
            "title": "List"
        }
    return render(request,"index.html", context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request): #update post
    return HttpResponse("<h1>Update</h1>")

def post_delete(request): #delete post
    return HttpResponse("<h1>Delete</h1>")