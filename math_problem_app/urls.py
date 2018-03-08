
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
    url(r'^lecture/', lecture, name='lecture'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^findPassword/', findPassword, name='findPassword'),
    url(r'^findPassword2/', findPassword2, name='findPassword2'),
    url(r'^findPassword3/', findPassword3, name='findPassword3'),
    url(r'^sendPasswordEmail/', sendPasswordEmail, name='sendPasswordEmail'),
    url(r'^changePassword/', changePassword, name='changePassword'),
    url(r'^board/', board, name='board'),
    url(r'^createTest/', createTest, name='createTest'),
    url(r'^problemBox/', problemBox, name='problemBox'),
    url(r'^ranking/', ranking, name='ranking'),

]
