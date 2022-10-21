from django.shortcuts import render
from .models import BlogPost
from django.contrib import messages

# Create your views here.
def blog_home(request):
  blog_posts = BlogPost.objects.filter(is_approved=True).order_by('-id')
  context = {
    'blog_posts': blog_posts
  }
  return render(request, 'blog/blog_home.html', context)

def blog_post(request, post_slug):
  try:
    post = BlogPost.objects.get(post_slug=post_slug)
  except:
    post = ''
  context = {
    'post': post
  }
  return render(request, 'blog/blog_post.html', context)

def add_blog(request):
  if request.method == 'POST':
    title = request.POST['title']
    author = request.POST['author']
    intro = request.POST['intro']
    body = request.POST['body']
    post_slug = title.lower()
    post_slug = post_slug.replace(' ', '-')

    try:
      post = BlogPost(
      title = title,
      post_slug = post_slug,
      author = author,
      intro = intro,
      body = body
    )
      post.save()
      messages.success(request, 'Post sent successfully, one of the site moderators will check your content and approve later.')
    except:
      messages.error(request, 'Something went wrong!!!, try again later, if the issue persists kindly inform the site moderators.')

  return render(request, 'blog/add_blog.html')