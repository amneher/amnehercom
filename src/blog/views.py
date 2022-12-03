import pytz
from datetime import timedelta

from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from .models import Post


def home(request):
	six_months_ago = timezone.localtime() - timedelta(days=180)
	posts = Post.objects.filter(created__gte=six_months_ago).order_by('-updated')

	return render(request, 'blog/templates/blog_list.html', {'posts': posts})

def post_detail(request, id):
	post = Post.objects.get(id=id)

	return render(request, 'blog/templates/blog_single.html', {'post': post})