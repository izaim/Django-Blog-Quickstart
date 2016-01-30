from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def post_create(request): #create post
    return HttpResponse("<h1>Create</h1>")

def post_detail(request): #read post
    instance = get_object_or_404(Post,id=1)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request,"single_post.html", context)
    #return HttpResponse("<h1>Detail</h1>")

def post_list(request): #list posts
    queryset = Post.objects.all()
    context ={
        "object_list": queryset,
        "title": "My User List"
    }
    # if request.user.is_authenticated():
    #     context ={
    #         "title": "My User List"
    #     }
    # else:
    #     context ={
    #         "title": "List"
    #     }
    return render(request,"index.html", context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request): #update post
    return HttpResponse("<h1>Update</h1>")

def post_delete(request): #delete post
    return HttpResponse("<h1>Delete</h1>")