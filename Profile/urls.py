import re
from xml.dom.minidom import Document
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from primerApp import settings

from Profile.views import TablaProfileList, TablaProfileDetail, ProfileUser


urlpatterns = [
    re_path(r'^profile/$', TablaProfileList.as_view()),
    re_path(r'^profile/(?P<pk>\d+)$', TablaProfileDetail.as_view()),
    re_path(r'^data/(?P<pk>\d+)/$',ProfileUser.as_view()),
]
