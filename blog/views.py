from django.shortcuts import render

posts = [
    {
        'author': 'scrublinux',
        'title': 'first blog post',
        'content': 'content of first post',
        'date_posted': 'June 28 2020',
    },
    {
        'author': 'jane doe',
        'title': '2nd blog post',
        'content': 'content of 2nd post',
        'date_posted': 'June 29 2020',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
