from django.test import TestCase
from django.urls import reverse
from .models import Post, Author, Tag

class AuthorModelTest(TestCase):
    def test_author_str(self):
        author = Author.objects.create(first_name="Jane", last_name="Doe", email="jane@example.com")
        self.assertEqual(str(author), "Jane Doe")

    def test_author_email_unique(self):
        Author.objects.create(first_name="Jane", last_name="Doe", email="jane@example.com")
        with self.assertRaises(Exception):
            Author.objects.create(first_name="John", last_name="Smith", email="jane@example.com")


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(tag="Django")
        self.assertEqual(str(tag), "Django")


class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Jane", last_name="Doe", email="jane@example.com")
        self.tag = Tag.objects.create(tag="Python")

    def test_post_creation(self):
        post = Post.objects.create(
            title="My First Post",
            excerpt="This is an excerpt.",
            slug="my-first-post",
            content="This is the content.",
            author=self.author
        )
        post.tags.add(self.tag)
        self.assertEqual(str(post), "My First Post")
        self.assertEqual(post.tags.count(), 1)


class ViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Jane", last_name="Doe", email="jane@example.com")
        self.tag = Tag.objects.create(tag="Python")
        self.post = Post.objects.create(
            title="Test Post",
            excerpt="Excerpt",
            slug="test-post",
            content="Some content",
            author=self.author
        )
        self.post.tags.add(self.tag)

    def test_starting_page_view(self):
        response = self.client.get(reverse('starting-page'))  # Asegúrate que esta url se llama así en urls.py
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_authors_list_view(self):
        response = self.client.get(reverse('authors-list'))  # Igual aquí, verifica el nombre de la URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.first_name)

    def test_tags_list_view(self):
        response = self.client.get(reverse('tags-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tag.tag)
