from django.shortcuts import render
from django.utils import timezone
from .models import Post
# . before models means "current directory/application"

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
