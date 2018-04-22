from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', TagList.as_view(), name="tag_list"),
    url(
        r'^(?P<pk>\d+)/detail/$',
        tag_detail,
        name='tag_detail'
    )

]