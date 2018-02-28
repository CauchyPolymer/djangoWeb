import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from math_problem_app.models import User


def main(request):
    if not User.objects.filter(email='mathadmin@math.co.kr'):
        user = User(email='mathadmin@math.co.kr').store()
        user.set_password('ql135cjs')
    return render(request, 'metronic_index.html', {'isLogged': True if request.session.get('userSrl') else False})


def returnHttpResponse(data):
    return HttpResponse(
        json.dumps(data),
        content_type="application/json; charset=utf8"
    )


def login(request):
    if request.POST.get('userEmail'):
        email = str(request.POST.get('userEmail'))
        password = str(request.POST.get('password'))

        if not User.objects.filter(email=email).exists():
            return returnHttpResponse({'success': False, 'msg': 'Check Your Email Please.'})

        user = User.objects.get(email=email)
        if not user.check_password(password):
            return returnHttpResponse({'success': False, 'msg': 'Check Your Password Please.'})

        request.session['userSrl'] = user.userSrl
        request.session.set_expiry(3600 * 24 * 7)  # 1 week

        return returnHttpResponse({'success': True, 'msg': 'Welcome Math Admin!'})


def logout(request):
    request.session.delete()
    return returnHttpResponse({'msg': "logout successfully"})