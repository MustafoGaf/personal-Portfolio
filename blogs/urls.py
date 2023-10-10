from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog, name="blog"),
   path("<int:blog_id>/", views.detail, name="blog_detail"),
   path('<int:blog_id>/share/', views.blog_share, name='blog_share'),
   path('<int:blog_id>/comment/', views.blog_comment, name='blog_comment'),
   path('tag/<slug:tag_slug>', views.blog, name='blog_list_by_tag'),
   # path('newblog/', views.newBlog, name='newBlog')
]