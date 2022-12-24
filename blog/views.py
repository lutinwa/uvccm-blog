from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.filter(status=1).order_by('-created_on')

	return render(request, "index.html", {'posts': posts})

def show(request, post_id):
	post = Post.objects.get(id=post_id)

	return render(request, "show.html", {"post": post})
def contact(request):

	return render(request, "contact.html")

def uongozi(request):
	return render(request, "uongozi.html")

def malengo(request):
	return render(request, "malengo.html")
