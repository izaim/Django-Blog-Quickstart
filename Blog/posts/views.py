from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


# Create your views here.
def post_create(request): #create post
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request,"Article Posted Successfully!", extra_tags="glyphicon glyphicon-ok")
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
        "title": "My Posts"
    }
    return render(request,"posts.html", context)


def post_update(request, id=None): #update post
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Article Edited Successfully!", extra_tags="glyphicon glyphicon-ok")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request,"form.html", context)


def post_delete(request, id=None): #delete post
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request,"Article Deleted Successfully!", extra_tags="glyphicon glyphicon-ok")
    return redirect("posts:list")