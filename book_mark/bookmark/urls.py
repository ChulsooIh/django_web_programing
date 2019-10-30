from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkList.as_view(), name='list'),
    path('add', BookmarkAdd.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetail.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDelete.as_view(), name='delete')
]