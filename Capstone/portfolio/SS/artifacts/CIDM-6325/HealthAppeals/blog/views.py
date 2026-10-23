from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "blog/home.html")


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # <--- important
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form): 
        user = form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    permission_required = "blog.change_post"


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
    permission_required = "blog.delete_post"


class UserLoginView(auth_views.LoginView):
    template_name = "blog/login.html"


class UserLogoutView(auth_views.LogoutView):
    template_name = "blog/logout.html"  # optional

class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
