from django.urls import path
from .views import *

urlpatterns = [
    path('generate-comments/https://www.instagram.com/<path:url>/', CommentGeneratorAPIView.as_view(), name='generate_comments')
]