from django.urls import path
from .views import home, blog_category, category, add_blog, blog_detail, blog_update, user_list

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>', blog_category, name='blog_category'),
    path('category_list', category, name='category_list'),
    path('add-blog', add_blog, name='add_blog'),
    path('blog/<slug:slug>', blog_detail, name='blog_detail'),
    path('blog-update/<slug:slug>', blog_update, name='blog_update'),
    path('user-list', user_list, name='user_list'),

]
