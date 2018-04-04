
from django.conf.urls import url
from django.conf.urls.static import static

from math_admin.views import *
from math_problem import settings

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^save_problem/', save_problem, name='save_problem'),
    url(r'^problem_photo/', problem_photo, name='problem_photo'),
    url(r'^problem/', problem, name='problem'),
    url(r'^create_board/', create_board, name='create_board'),
    url(r'^new_users/', new_users, name='new_users'),
    url(r'^users/', users, name='users'),
    url(r'^id_certificate/', id_certificate, name='id_certificate'),
]

