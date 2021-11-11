from django.urls import path
from .views import *

urlpatterns = [
      path('', NewsViews.as_view()),
      path('<int:pk>', Post.as_view()),
      path('search/', NewsSearch.as_view()),
      path('add/', NewsCreateView.as_view(), name='news_create'),
      path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
      path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
      path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),

]