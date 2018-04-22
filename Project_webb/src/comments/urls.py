from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', CommentList.as_view(), name="comment_list"),
]