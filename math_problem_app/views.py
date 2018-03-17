import json
import random

import re
import uuid

import datetime
from functools import reduce

import mandrill
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from math_problem import settings
from math_problem_app.sendSms import sendSms
from math_problem_app.models import User, Problem, ProblemUnit, Photo, Board, Test, Comment, Answer, AnswerNum, Rating, \
    Score


def head(request):
    user = None
    if request.session.get('userId'):
        user = User.objects.get(id=str(request.session.get('userId')))
    return render(request, 'head.html', {'user': user})


def main(request):
    user = None
    if request.session.get('userId'):
        user = User.objects.get(id=str(request.session.get('userId')))
    return render(request, 'main.html', {'user': user})


def signIn(request):
    return render(request, 'signIn.html')


def signIn2(request):
    return render(request, 'signIn2.html')


def signIn3(request):
    user = getLoginUser(request)
    return render(request, 'signIn3.html', {'user': user})


def mypage(request):
    user = getLoginUser(request)
    if user:
        return render(request, 'mypage.html', {'user': user})
    else:
        return render(request, 'login.html')


def mypage2(request):
    user = getLoginUser(request)
    return render(request, 'mypage2.html', {'user': user})


def returnHttpResponse(data):
    return HttpResponse(
        json.dumps(data),
        content_type="application/json; charset=utf8"
    )


def getLoginUser(request):
    if request.session.get('userId'):
        id = str(request.session.get('userId'))
    else:
        return False
    return User.objects.get(id=id)


def idDuplicate(request):
    id = str(request.GET.get('id'))
    if not re.match("^[A-Za-z0-9_-]*$", id):
        return returnHttpResponse({'success': False, 'msg': '아이디를 영문과 숫자로만 입력해 주세요.'})
    if len(id) < 4:
        return returnHttpResponse({'success': False, 'msg': '아이디를 4자 이상 입력해 주세요.'})
    if User.objects.filter(id=id).exists():
        return returnHttpResponse({'success': False, 'msg': '아이디가 중복 됩니다.'})

    return returnHttpResponse({'success': True, 'msg': '사용 가능한 아이디 입니다.'})


@csrf_exempt
def signUp(request):
    id = str(request.POST.get('id'))
    password = str(request.POST.get('password'))
    name = str(request.POST.get('name'))
    sex = str(request.POST.get('sex'))
    phone = str(request.POST.get('phone'))
    email = str(request.POST.get('email'))
    school = str(request.POST.get('school'))
    grade = str(request.POST.get('grade'))

    user = User(id=id, name=name, sex=sex, phone=phone, email=email, school=school, grade=grade).store()
    user.set_password(password)
    user.save()

    request.session['userId'] = user.id

    return returnHttpResponse({'success': True, 'msg': '회원가입이 완료 되었습니다.'})


def getRateData(request):
    user = getLoginUser(request)
    if not user or not user.rate:
        return returnHttpResponse([{'label' : '1등급', 'y': 1}, {'label' : '3등급', 'y': 3}, {'label' : '2등급', 'y': 2}, {'label' : '1등급', 'y': 1},
                {'label' : '2등급', 'y': 2}, {'label' : '1등급', 'y': 1}])

    if request.GET.get('ratingSrl'):
        rate = Rating.objects.get(ratingSrl=int(request.GET.get('ratingSrl')))
    else:
        rate = user.rate.last()

    data = [{'label': str(rate.su1) + '등급', 'y': rate.su1}, {'label': str(rate.su2) + '등급', 'y': rate.su2},
            {'label': str(rate.mi1) + '등급', 'y': rate.mi1}, {'label': str(rate.mi2) + '등급', 'y': rate.mi2},
            {'label': str(rate.givec) + '등급', 'y': rate.givec}, {'label': str(rate.hwaktong) + '등급', 'y': rate.hwaktong}]

    return returnHttpResponse(data)


def estimationStart(request):
    user = getLoginUser(request)
    if user:
        return render(request, 'estimationStart.html')
    else:
        return render(request, 'login.html')


def createLecture(request):
    return render(request, 'createLecture.html')


def googled92c898637781d67(request):
    return render(request, 'googled92c898637781d67.html')


def lecture(request):
    return render(request, 'lecture.html')


@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        id = str(request.POST.get('id'))
        password = str(request.POST.get('password'))
        loginStay = str(request.POST.get('loginStay'))

        print(loginStay)

        if not User.objects.filter(id=id).exists():
            return returnHttpResponse({'success': False, 'msg': '해당 아이디가 존재 하지 않습니다.'})

        user = User.objects.get(id=id)
        if not user.check_password(password):
            return returnHttpResponse({'success': False, 'msg': '비밀번호가 틀렸습니다.'})

        request.session['userId'] = user.id
        if loginStay == 'true':
            request.session.set_expiry(3600 * 24 * 7) # 7일
        return returnHttpResponse({'success': True, 'msg': id +'님 환영합니다.'})


def logout(request):
    request.session.delete()
    return returnHttpResponse({'msg': '로그아웃 되었습니다.'})


def findPassword(request):
    return render(request, 'findPassword.html')


def findPassword2(request):
    return render(request, 'findPassword2.html')


def sendPasswordEmail(request):
    email = str(request.GET.get('email'))
    key = str(uuid.uuid4())[:6]
    msg = '수능 대왕 비밀번호 변경 인증 키는\n' + key + '\n 입니다.'
    if not send_email('수능 대왕 비밀번호 변경', msg, email, ''):
        return returnHttpResponse({'success': False, 'msg': '이메일이 전송되지 않았습니다.'})
    request.session['key'] = key
    return returnHttpResponse({'success': True, 'msg': '이메일이 정상적으로 보내졌습니다.'})


@csrf_exempt
def changePassword(request):
    id = str(request.POST.get('id'))
    password = str(request.POST.get('password'))
    key = str(request.POST.get('key'))
    if key != str(request.session.get('key')):
        return returnHttpResponse({'success': False, 'msg': '인증 키 값이 잘못 입력되었습니다.'})

    if not User.objects.filter(id=id).exists():
        return returnHttpResponse({'success': False, 'msg': '해당 아이디가 존재 하지 않습니다.'})
    user = User.objects.get(id=id)
    user.set_password(password)
    user.save()

    return returnHttpResponse({'success': True, 'msg': '비밀번호가 올바르게 변경 되었습니다.'})


def findPassword3(request):
    return render(request, 'findPassword3.html')


def send_email(title, body, to_email, to_name):
    try:
        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
        message = {'auto_html': None,
                   'auto_text': None,
                   'from_email': 'contact@sndw.co.kr',
                   'from_name': 'BeautySocial',
                   'headers': {'Reply-To': 'contact@sndw.co.kr'},
                   # 'html': '<p>Example HTML content</p>',
                   'text': body,
                   'important': False,
                   'inline_css': None,
                   'merge': True,
                   'merge_language': 'mailchimp',
                   'metadata': {'website': 'http://sndw.co.kr'},
                   'preserve_recipients': None,
                   'return_path_domain': None,
                   'signing_domain': None,
                   'subject': title,
                   'to': [{'email': to_email,
                           'name': to_name,
                           'type': 'to'}],
                   'track_clicks': None,
                   'track_opens': None,
                   'tracking_domain': None,
                   'url_strip_qs': None,
                   'view_content_link': None}

        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool',
                                               send_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        '''
        [{'_id': 'abc123abc123abc123abc123abc123',
          'email': 'recipient.email@example.com',
          'reject_reason': 'hard-bounce',
          'status': 'sent'}]
        '''
        print(result)
        return True
    except mandrill.Error as e:
        # Mandrill errors are thrown as exceptions
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        return False


def board(request):
    user = getLoginUser(request)
    if user:
        return render(request, 'board.html')
    else:
        return render(request, 'login.html')


def boardContents(request):
    type = int(request.GET.get('type'))
    keyword = str(request.GET.get('keyword'))

    idx = int(request.GET.get('idx'))
    size = int(request.GET.get('size'))

    boards = Board.objects.filter(type=type)

    if keyword is not '':
        boards = boards.filter(Q(title__contains=keyword) | Q(text__contains=keyword))

    return render(request, 'boardContent.html', {'boards': boards.order_by('-createdAt')[idx: idx + size]})


@csrf_exempt
def createTest(request):
    user = getLoginUser(request)
    if request.method == 'GET':
        if user:
            return render(request, 'createTest.html', {'user': user})
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        problemSrls = str(request.POST.get('problemSrls'))
        type = int(request.POST.get('problemType'))
        name = str(request.POST.get('name'))
        if request.POST.get('testSrl'):
            test = Test.objects.get(testSrl=int(request.POST.get('testSrl')))
        else:
            test = Test(type=type).store()

        test.problems.clear()
        if problemSrls:
            for problemSrl in problemSrls.split(','):
                if len(problemSrl) > 0:
                    test.problems.add(Problem.objects.get(problemSrl=problemSrl))
                    test.scores.add(Score(score=5).store())

        test.name = name
        test.save()
        user.tests.add(test)
        user.save()

        return render(request, 'testBox.html', {'tests': user.tests.all()})


def problemBox(request):
    idx = int(request.GET.get('idx'))
    size = int(request.GET.get('size'))
    type1 = int(request.GET.get('type1'))
    type2 = int(request.GET.get('type2'))
    difficulty = int(request.GET.get('difficulty'))
    testSrl = int(request.GET.get('testSrl')) if request.GET.get('testSrl') not in ['', 'undefined'] else None

    problems = Problem.objects.filter(type1=type1, type2=type2, difficulty=difficulty)

    problems = problems[idx:idx+size]

    testProblemSrls = None
    if testSrl and Test.objects.get(testSrl=testSrl).problems.all():
        testProblemSrls = list(reduce(lambda x, y: x + y, map(lambda x: [x['problemSrl']], Test.objects.get(testSrl=testSrl).problems.all().values('problemSrl'))))

    return render(request, 'problemBox.html', {'problems': problems, 'testProblemSrls': testProblemSrls})


def ranking(request):
    return render(request, 'ranking.html')


def testBox(request):
    user = getLoginUser(request)
    return render(request, 'testBox.html', {'tests': user.tests.all()})


@csrf_exempt
def phoneCert(request):
    if request.method == 'GET':
        phone = str(request.GET.get('phone'))
        key = random.randint(1000, 9999)
        request.session['key'] = key

        sendSms(phone, '수능대왕 폰 인증 번호 입니다. ['+str(key)+']')

        return returnHttpResponse({'success': True, 'msg': '문자 발송에 성공하였습니다.'})

    elif request.method == 'POST':
        key = str(request.POST.get('key'))
        if str(request.session['key']) == key:
            return returnHttpResponse({'success': True, 'msg': '핸드폰 인증에 성공하였습니다.'})

        return returnHttpResponse({'success': False, 'msg': '인증번호를 확인해 주세요.'})


def boardDetail(request):
    user = getLoginUser(request)
    boardSrl = int(request.GET.get('boardSrl'))
    board = Board.objects.get(boardSrl=boardSrl)
    board.viewCnt += 1
    board.save()
    return render(request, 'boardDetail.html', {'board': board, 'user': user})


@csrf_exempt
def comment(request):
    user = getLoginUser(request)

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        text = str(request.POST.get('text'))
        boardSrl = int(request.POST.get('boardSrl'))
        commentSrl = int(request.POST.get('commentSrl')) if request.POST.get('commentSrl') else None
        if commentSrl:
            comment = Comment.objects.get(commentSrl=commentSrl)
            comment.writer = user
            comment.text = text
        else:
            comment = Comment(writer=user, text=text).store()

        comment.save()

        board = Board.objects.get(boardSrl=boardSrl)
        board.comments.add(comment)

        return render(request, 'comments.html', {'board': board, 'user': user})

    elif request.method == 'DELETE':
        commentSrl = int(request.GET.get('commentSrl'))
        boardSrl = int(request.GET.get('boardSrl'))
        board = Board.objects.get(boardSrl=boardSrl)
        board.comments.remove(Comment.objects.get(commentSrl=commentSrl))


        return render(request, 'comments.html', {'board': board, 'user': user})


@csrf_exempt
def createBoard(request):
    user = getLoginUser(request)
    if request.method == 'GET':
        return render(request, 'createBoard.html', {'user': user})
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        type = request.POST.get('type')
        board = Board(title=title, text=text, type=type, writer=user).store()

        return returnHttpResponse({'success': True, 'msg':'게시판 글이 작성 되었습니다.'})


def onlineEstimationStart(request):
    tests = Test.objects.filter(type=2)  # 진단고사
    randomIdx = random.randint(0, tests.count() - 1)
    request.session['testSrl'] = tests[randomIdx].testSrl
    return render(request, 'onlineEstimationStart.html')


def estimation(request):
    problemIdx = int(request.GET.get('problemIdx'))
    if request.GET.get('testSrl'):
        test = Test.objects.get(testSrl=int(request.GET.get('testSrl')))
    else:
        test = Test.objects.get(testSrl=int(request.session.get('testSrl')))
    return render(request, 'estimation.html', {'test': test, 'problem': test.problems.all()[problemIdx], 'problemIdx': problemIdx + 1, 'from': str(request.GET.get('from'))})


@csrf_exempt
def answer(request):
    user = getLoginUser(request)
    if request.method == 'POST':
        try:
            answers = str(request.POST.get('answers'))
        except SyntaxError or ValueError:
            return returnHttpResponse({'success': False, 'msg': '정답을 모두 적지 않았습니다.'})
        testSrl = int(request.POST.get('testSrl'))
        test = Test.objects.get(testSrl=testSrl)
        answer = Answer(test=test).store()
        for ans in answers.split(','):
            try:
                answer.answers.add(AnswerNum(answer=ans).store())
            except ValueError:
                return returnHttpResponse({'success': False, 'msg': '정답을 모두 적지 않았습니다.'})

        answer.save()
        user.answers.add(answer)

        rate = calcRating(test, answer)
        user.rate.add(rate)
        user.save()

        if str(request.POST.get('from')) == 'estimation':
            return render(request, 'estimationResult.html', {'rate': rate, 'test': test, 'answers': answer})
        elif str(request.POST.get('from')) == 'test':
            return render(request, 'testResult.html', {'rate': rate, 'test': test, 'answers': answer})


def calcRating(test, answer):
    su1 = 0; su2 = 0; mi1 = 0; mi2 = 0; hwaktong = 0; givec = 0
    su1tot = 0; su2tot = 0; mi1tot = 0; mi2tot = 0; hwaktongtot = 0; givectot = 0
    problems = test.problems.all()
    scores = test.scores.all()
    totalScore = 0
    rightScore = 0
    for i, ans in enumerate(answer.answers.all()):
        problem = problems[i]
        problem.totalAnswered += 1
        score = scores[i].score
        totalScore += score
        units = list(map(lambda x: x['unit'], problem.unit.values('unit')))
        if 1 in units:
            su1tot += score
        if 2 in units:
            su2tot += score
        if 3 in units:
            mi1tot += score
        if 4 in units:
            mi2tot += score
        if 5 in units:
            hwaktongtot += score
        if 6 in units:
            givectot += score

        if problem.answer == ans.answer:
            if 1 in units:
                su1 += score
            if 2 in units:
                su2 += score
            if 3 in units:
                mi1 += score
            if 4 in units:
                mi2 += score
            if 5 in units:
                hwaktong += score
            if 6 in units:
                givec += score
            problem.rightAnswered += 1
            rightScore += score
        problem.save()

    su1rate = (int((1 - su1 / su1tot) * 10) if su1 / su1tot != 1 else 1) if su1 != 0 else 9
    su2rate = (int((1 - su2 / su2tot) * 10) if su2 / su2tot != 1 else 1) if su2 != 0 else 9
    mi1rate = (int((1 - mi1 / mi1tot) * 10) if mi1 / mi1tot != 1 else 1) if mi1 != 0 else 9
    mi2rate = (int((1 - mi2 / mi2tot) * 10) if mi2 / mi2tot != 1 else 1) if mi2 != 0 else 9
    hwaktongrate = (int((1 - hwaktong / hwaktongtot) * 10) if hwaktong / hwaktongtot != 1 else 1) if hwaktong != 0 else 9
    givecrate = (int((1 - givec / givectot) * 10) if givec / givectot != 1 else 1) if givec != 0 else 9

    return Rating(score=rightScore, totalScore=totalScore, su1=su1rate, su2=su2rate, mi1=mi1rate, mi2=mi2rate, hwaktong=hwaktongrate, givec=givecrate).store()


def testProblems(request):
    testSrl = int(request.GET.get('testSrl'))
    test = Test.objects.get(testSrl=testSrl)

    return render(request, 'testProblems.html', {'test': test, 'problems': test.problems.all(), 'from':'testStart'})