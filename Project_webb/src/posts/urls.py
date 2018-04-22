from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', PostList.as_view(), name="post_list"),
    url(
            r'^(?P<pk>\d+)/detail/$',
            post_detail,
            name = 'post_detail'
        )
]