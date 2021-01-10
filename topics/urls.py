from django.urls import path

from topics.views import TopicCreate, TopicListView, TopicDetailView, TopicUpdate, TopicDelete

urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('add/', TopicCreate.as_view(), name='topic-add'),
    path('<int:pk>/update/', TopicUpdate.as_view(), name='topic-update'),
    path('<int:pk>/delete/', TopicDelete.as_view(), name='topic-delete'),
]
