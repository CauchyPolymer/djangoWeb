
from django.conf.urls import url

from math_problem_app.views import *

urlpatterns = [
    url(r'^$', main, name='main'),
    # url(r'^login/', login, name='login'),

]
