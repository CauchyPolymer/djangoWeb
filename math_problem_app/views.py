import json

import re
import uuid

import datetime
import mandrill
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from math_problem import settings
from math_problem_app.models import User, Problem, ProblemUnit, Photo, Board


def head(request):
    return render(request, 'head.html')


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

    data = [{'label': str(user.rate.su1) + '등급', 'y': user.rate.su1}, {'label': str(user.rate.su2) + '등급', 'y': user.rate.su2},
            {'label': str(user.rate.mi1) + '등급', 'y': user.rate.mi1}, {'label': str(user.rate.mi2) + '등급', 'y': user.rate.mi2},
            {'label': str(user.rate.givec) + '등급', 'y': user.rate.givec}, {'label': str(user.rate.hwaktong) + '등급', 'y': user.rate.hwaktong}]

    return returnHttpResponse(data)


def estimationStart(request):
    return render(request, 'estimationStart.html')


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
    return render(request, 'board.html')


def boardContents(request):
    type = int(request.GET.get('type'))
    keyword = str(request.GET.get('keyword'))

    idx = int(request.GET.get('idx'))
    size = int(request.GET.get('size'))

    boards = Board.objects.filter(type=type)

    if keyword is not '':
        boards = boards.filter(Q(title__contains=keyword) | Q(text__contains=keyword))

    return render(request, 'board_content.html', {'boards': boards.order_by('-createdAt')[idx: idx + size]})


def createTest(request):
    user = getLoginUser(request)
    return render(request, 'createTest.html', {'user': user})


def problemBox(request):
    idx = int(request.GET.get('idx'))
    size = int(request.GET.get('size'))
    type = str(request.GET.get('type')).split(',') if len(str(request.GET.get('type'))) > 0 else []
    difficulty = int(request.GET.get('difficulty'))

    problems = Problem.objects.filter(type__in=type, difficulty=difficulty)

    problems = problems[idx:idx+size]

    return render(request, 'problemBox.html', {'problems': problems})


def ranking(request):
    return render(request, 'ranking.html')


def test(request):
    return render(request, 'test.html')
