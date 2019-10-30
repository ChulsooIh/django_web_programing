from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/result', ResultView.as_view(), name='result'),
    path('<int:pk>/vote', vote, name='vote'),
    path('api/', ApiQuestionList.as_view(), name="api_list"),
    path('api/<int:pk>/', ApiQuestionDetail.as_view(), name="api_detail")
]