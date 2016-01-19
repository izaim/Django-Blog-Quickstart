from django.http import HttpResponse


# Create your views here.
def post_create(request): #create post
    return HttpResponse("<h1>Create</h1>")

def post_detail(request): #read post
    return HttpResponse("<h1>Detail</h1>")

def post_list(request): #list posts
    return HttpResponse("<h1>List</h1>")

def post_update(request): #update post
    return HttpResponse("<h1>Update</h1>")

def post_delete(request): #delete post
    return HttpResponse("<h1>Delete</h1>")