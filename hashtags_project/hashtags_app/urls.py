from django.urls import path
from .views import RemoveHashtagsView, GetHashtagsView, ReplaceHashtagsView, CountHashtagsView

urlpatterns = [
    path('remove-hashtags/', RemoveHashtagsView.as_view(), name='remove_hashtags'),
    path('get-hashtags/', GetHashtagsView.as_view(), name='get_hashtags'),
    path('replace-hashtags/', ReplaceHashtagsView.as_view(), name='replace_hashtags'),
    path('count-hashtags/', CountHashtagsView.as_view(), name='count_hashtags'),
]
