from django.urls import path
from blog.api_views import get_blog_by_id

url_patterns =[
    path('view/',get_blog_by_id)
]
