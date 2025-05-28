from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(default="Excerpt not provided")
    image_name = models.CharField(max_length=100, default="postimg.jpeg")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts", null=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    tag = models.CharField(max_length=100, default="Uncategorized")


    def __str__(self):
        return self.tag
    
