from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/>', views.post_delete, name='post_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('user/', views.user_post_list, name='user_post_list'),
    path('user/post/<int:pk>/', views.user_post_detail, name='user_post_detail'),
]