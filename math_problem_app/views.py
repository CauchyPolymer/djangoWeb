import json

import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from math_problem_app.models import User


def main(request):
    return render(request, 'main.html')


def signIn(request):
    return render(request, 'signIn.html')


def signIn2(request):
    return render(request, 'signIn2.html')


def signIn3(request):
    user = User.objects.get(id=request.session['userId'])
    return render(request, 'signIn3.html', {'user': user})


def mypage(request):
    return render(request, 'mypage.html')


def returnHttpResponse(data):
    return HttpResponse(
        json.dumps(data),
        content_type="application/json; charset=utf8"
    )


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