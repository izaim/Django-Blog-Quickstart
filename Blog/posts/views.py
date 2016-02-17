from urllib import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post

from django.shortcuts import render


# Create your views here.
def post_create(request): #create post
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
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


def post_detail(request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        context = {
            "title": instance.title,
            "instance": instance,
        }
        return render(request, "single_post.html", context)


def post_list(request): #list posts
    queryset_list = Post.objects.all().order_by("-created")
    paginator = Paginator(queryset_list, 5) #Show 25 contacts per page

    #pagination
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context ={
        "object_list": queryset,
        "title": "My Posts"
    }

    return render(request,"posts.html", context)


def post_update(request, slug=None): #update post
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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


def post_delete(request, slug=None): #delete post
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request,"Article Deleted Successfully!", extra_tags="glyphicon glyphicon-ok")
    return redirect("posts:list")