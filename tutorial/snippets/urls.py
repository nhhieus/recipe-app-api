from django.urls import path
from snippets.views import SnippetList, SnippetDetail

app_name = 'snippets'

urlpatterns = [
    path('', SnippetList.as_view(), name='snippet_list'),
    path('<int:pk>/', SnippetDetail.as_view(), name='snippet_detail'),
]