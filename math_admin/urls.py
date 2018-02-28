
from django.conf.urls import url

from math_admin.views import *

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),

]
