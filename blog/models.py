from django.db import models
from django.urls import reverse
from PIL import Image
from user.models import User

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class FeaturedPost(models.Model):
    quote = models.OneToOneField(Quote, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='featured_post_images/', default='default/featured-post.jpg')

    def __str__(self):
        return '{} {}'.format(self.title, self.quote.author)

class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    sub_intro = models.TextField(blank=True)
    sub_title = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    quote = models.OneToOneField(Quote, on_delete=models.CASCADE)
    highlighted_text = models.TextField(blank=True)
    post_body_left = models.TextField(blank=True)
    post_body_right = models.TextField(blank=True)
    youtube_link = models.URLField(blank=True)
    post_footer = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.author.name, self.title)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.tag_name


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        size = (500, 750)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(self.image.path)

    def __str__(self):
        return self.image.path

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    picture = models.ImageField(upload_to='comments_author/', default='default/comments_author.jpg')
    created_at = models.DateTimeField(auto_now=True)
    comment_author = models.CharField(max_length=255, blank=True)
    comment_body = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return 'Post: ' + self.post.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)
        size = (108, 108)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(self.picture.path)