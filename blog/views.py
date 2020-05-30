from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import FeaturedPost, PostImage, Post, Tag, Comment
from user.models import User
from .forms import CommentForm

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['featured_posts'] = FeaturedPost.objects.all()
        context['posts'] = Post.objects.all()
        context['posts_count'] = Post.objects.all().count()
        context['images'] = PostImage.objects.all()
        context['tags'] = Tag.objects.all()
        context['author'] = User.objects.first()
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        images = PostImage.objects.filter(post=post)
        tags = Tag.objects.filter(post=post)
        author = post.author
        comments = Comment.objects.filter(post=post)
        comments_cnt = Comment.objects.filter(post=post).count()
        context['post'] = post
        context['images'] = images
        context['tags'] = tags
        context['author'] = author
        context['comments'] = comments
        context['comments_cnt'] = comments_cnt
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, **kwargs):
        post = self.get_object()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid():
                name = request.POST.get('comment_author')
                email = request.POST.get('email')
                message = request.POST.get('comment_body')
                comment = Comment.objects.create(post=post, comment_author=name, email=email, comment_body=message)
                comment.save()
                post1 = Post.objects.get(pk=post.pk)
                return redirect(post1)