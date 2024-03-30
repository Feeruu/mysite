from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#def post_list(request):
    #if request.user.is_superuser:
        #return redirect('admin_panel')  # Перенаправление на страницу администратора
    #else:
        #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        #return render(request, 'blog/post_list.html', {'posts': posts})
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):
    if request.user.is_superuser:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        return redirect('user_post_list')

def user_post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/user_post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def user_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/user_post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            if request.user.is_superuser:
                return redirect('post_detail', pk=post.pk)
            else:
                return redirect('user_post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('post_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})