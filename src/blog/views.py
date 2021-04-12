import pytz
from datetime import datetime, timedelta

from django.shortcuts import render
from django.conf import settings

from .models import Post


def home(request):
	six_months_ago = datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) - timedelta(days=180)
	posts = Post.objects.filter(created__gte=six_months_ago).order_by('updated')

	return render(request, 'blog/templates/blog_list.html', {'posts': posts})

def post_detail(request, id):
	post = Post.objects.get(id=id)

	return render(request, 'blog/templates/blog_single.html', {'post': post})