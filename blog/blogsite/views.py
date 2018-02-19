from django.shortcuts import render
from .models import Post
from django.template import RequestContext

# Create your views here.
def posts(request):
	posts = Post.objects.all()

	#return render(request, 'blogsite/posts.html', {})
	return render(request, 'blogsite/posts.html', {'posts': posts})

def create_post(request):
	context_instance = RequestContext(request)
	post = Post(title='New post from code', content='New post content from code')
	post.save()
