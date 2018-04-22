from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', QuestionList.as_view(), name="question_list"),

    url(
        r'^(?P<pk>\d+)/detail/$',
        question_detail,
        name = 'question_detail'
    )
]