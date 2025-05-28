# views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {'authors': authors})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', {'tags': tags})


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = author.posts.all()

    return render(request, "blog/author_detail.html", {
        "author": author,
        "posts": posts,
    })

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.post_set.all()
    return render(request, "blog/tag_detail.html", {"tag": tag, "posts": posts})