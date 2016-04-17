from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_create(request):
    return HttpResponse("<h1>Create Moon</h1>")

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title" : "List",
        "object_list" : queryset
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title" : "My user list"
    #     }
    # else:
    #     context = {
    #         "title" : "List"
    #     }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update Moon</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete Moon</h1>")