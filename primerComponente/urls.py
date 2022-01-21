from django.urls import path, re_path
from django.conf.urls import include

from primerComponente.views import PrimerTablaList

urlpatterns = [
   re_path(r'^', PrimerTablaList.as_view()),
]