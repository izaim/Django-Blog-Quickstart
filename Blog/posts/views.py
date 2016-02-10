from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post


# Create your views here.
def post_create(request): #create post
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        print "Post Created Successfully."
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }

    return render(request,"form.html", context)

def post_detail(request, id): #read post
    instance = get_object_or_404(Post,id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request,"single_post.html", context)

def post_list(request): #list posts
    queryset = Post.objects.all()
    context ={
        "object_list": queryset,
        "title": "My User List"
    }
    return render(request,"index.html", context)

def post_update(request, id=None): #update post
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        print "Post Edited Successfully."
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request,"form.html", context)

def post_delete(request): #delete post
    return HttpResponse("<h1>Delete</h1>")