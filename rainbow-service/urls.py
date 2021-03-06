
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
    url(r'^idDuplicate/', idDuplicate, name='id_duplicate'),
    url(r'^getRateData/', getRateData, name='getRateData'),
    url(r'^getTestData/', getTestData, name='getTestData'),
    url(r'^getSmallUnitData/', getSmallUnitData, name='getSmallUnitData'),
    url(r'^getStudyTotalCount/', getStudyTotalCount, name='getStudyTotalCount'),
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
    url(r'^boardContents/', boardContents, name='boardContents'),
    url(r'^createTest/', createTest, name='createTest'),
    url(r'^problemBox/', problemBox, name='problemBox'),
    url(r'^ranking/', ranking, name='ranking'),
    url(r'^testBox/', testBox, name='testBox'),
    url(r'^phoneCert/', phoneCert, name='phoneCert'),
    url(r'^boardDetail/', boardDetail, name='boardDetail'),
    url(r'^comment/', comment, name='comment'),
    url(r'^createBoard/', createBoard, name='createBoard'),
    url(r'^onlineEstimationStart/', onlineEstimationStart, name='onlineEstimationStart'),
    url(r'^estimation/', estimation, name='estimation'),
    url(r'^answer/', answer, name='answer'),
    url(r'^testProblems/', testProblems, name='testProblems'),
    url(r'^recommend/', recommend, name='recommend'),
    url(r'^recommendTest/', recommendTest, name='recommendTest'),
    url(r'^recommendPage/', recommendPage, name='recommendPage'),
    url(r'^project/', project, name='project'),
    url(r'^getSmallUnitCount/', getSmallUnitCount, name='getSmallUnitCount'),
    url(r'^getSmallUnitTest/', getSmallUnitTest, name='getSmallUnitTest'),
    url(r'^getMiddleUnitLecture/', getMiddleUnitLecture, name='getMiddleUnitLecture'),
    url(r'^paymentStart/', paymentStart, name='paymentStart'),
    url(r'^privacy/', privacy, name='privacy'),
    url(r'^usage/', usage, name='usage'),
    url(r'^photo/', photo, name='photo'),
    url(r'^lectureBox/', lectureBox, name='lectureBox'),





]


