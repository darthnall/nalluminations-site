from django.shortcuts import render

def blog_home(request):
    context = { "title": "Blog" }
    return render(request, "blog/home.html", context=context)
