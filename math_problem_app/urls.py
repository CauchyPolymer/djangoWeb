
from django.conf.urls import url

from math_problem_app.views import *

urlpatterns = [
    url(r'^$', head, name='head'),
    url(r'^main/', main, name='main'),
    url(r'^signIn/', signIn, name='signIn'),
    url(r'^signIn2/', signIn2, name='signIn2'),
    url(r'^signIn3/', signIn3, name='signIn3'),
    url(r'^signUp/', signUp, name='signUp'),
    url(r'^mypage/', mypage, name='mypage'),
    url(r'^mypage2/', mypage2, name='mypage2'),
    url(r'^idDuplicate/', idDuplicate, name='id_duplicate'),
    url(r'^getRateData/', getRateData, name='getRateData'),
    url(r'^estimationStart/', estimationStart, name='estimationStart'),
    url(r'^createLecture/', createLecture, name='createLecture'),
    url(r'^googled92c898637781d67.html/', googled92c898637781d67, name='googled92c898637781d67.html'),
]
