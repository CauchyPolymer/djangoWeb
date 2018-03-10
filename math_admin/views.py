import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from math_problem_app.models import User, Problem, ProblemUnit, Photo, Board
from math_problem_app.views import getLoginUser


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
        request.session['userId'] = user.id
        request.session.set_expiry(3600 * 24 * 7)  # 1 week

        return returnHttpResponse({'success': True, 'msg': 'Welcome Math Admin!'})


def logout(request):
    request.session.delete()
    return returnHttpResponse({'msg': "logout successfully"})


def save_problem(request):
    text = str(request.POST.get('problemText'))
    answer = str(request.POST.get('answer'))
    type = str(request.POST.get('type'))
    difficulty = str(request.POST.get('difficulty'))
    unit = str(request.POST.get('unit'))

    if request.session.get('problemSrl'):
        problem = Problem.objects.get(problemSrl=int(request.session.get('problemSrl')))
        problem.text = text
        problem.answer = int(answer)
        problem.type = int(type)
        problem.difficulty = int(difficulty)
    else:
        problem = Problem(text=text, answer=int(answer), type=int(type), difficulty=int(difficulty)).store()

    if len(unit) > 0:
        for u in unit.split(','):
            problem.unit.add(ProblemUnit(unit=u).store())

    problem.save()

    request.session['problemSrl'] = None

    return render(request, 'basic_info/image_list.html')


def problem_photo(request):
    image = request.FILES.get('photo')
    photo = Photo(photo=image).store()
    if request.session.get('problemSrl'):
        problem = Problem.objects.get(problemSrl=int(request.session.get('problemSrl')))
    else:
        problem = Problem().store()
    problem.photos.add(photo)
    problem.store()

    request.session['problemSrl'] = problem.problemSrl

    return render(request, 'basic_info/image_list.html', {'problem': problem})


def problem(request):
    return render(request, 'basic_info/problem.html')


def create_board(request):
    if request.method == 'GET':
        return render(request, 'board/create_board.html', {'isNew': True})

    if request.method == 'POST':
        user = getLoginUser(request)
        type = int(request.POST.get('type'))
        title = str(request.POST.get('title'))
        text = str(request.POST.get('text'))
        if request.POST.get('boardSrl'):
            board = Board.objects.get(boardSrl=int(request.POST.get('boardSrl')))
            board.type = type
            board.title = title
            board.text = text
            board.writer = user
            board.save()
        else:
            board = Board(type=type, title=title, text=text, writer=user).store()

        return returnHttpResponse({'msg': '정상적으로 등록되었습니다.'})









