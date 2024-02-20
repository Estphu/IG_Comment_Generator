from rest_framework import generics
from .models import InstagramPost, Comment
from .serializers import InstagramPostSerializer, CommentSerializer

class CommentGeneratorAPIView(generics.ListAPIView):
    ''' Listing 10 dummy comments by taking Instagram URL '''
    serializer_class = CommentSerializer

    def get_queryset(self):
        url = self.kwargs['url']
        # Generate 10 dummy comments for the Instagram post URL
        comments = []
        for i in range(1, 11):
            comments.append({'text': f'Comment {i} for https://www.instagram.com/{url}'})
        return comments