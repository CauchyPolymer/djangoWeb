import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from math_problem_app.models import Problem, ProblemUnit, Photo, Board, User, MIDDLE_UNIT, SMALL_UNIT, \
    ProblemMiddleUnit, ProblemSmallUnit
from math_problem_app.views import getLoginUser


def main(request):
    if not User.objects.filter(email='mathadmin@math.co.kr'):
        user = User(email='mathadmin@math.co.kr').store()
        user.set_password('ql135cjs')
        user.id = 'admin'
        user.save()
    return render(request, 'metronic_index.html', {'isLogged': True if request.session.get('userSrl') else False,
                                                   'middleUnit': MIDDLE_UNIT, 'smallUnit': SMALL_UNIT})


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


@csrf_exempt
def save_problem(request):
    text = str(request.POST.get('problemText'))
    answer = str(request.POST.get('answer'))
    type1 = int(request.POST.get('type1'))
    type2 = int(request.POST.get('type2'))
    difficulty = str(request.POST.get('difficulty'))
    unit = str(request.POST.get('unit'))
    middleUnit = str(request.POST.get('middleUnit'))
    smallUnit = str(request.POST.get('smallUnit'))
    explanation = str(request.POST.get('explanation'))

    if request.session.get('problemSrl'):
        problem = Problem.objects.get(problemSrl=int(request.session.get('problemSrl')))
        problem.text = text
        problem.answer = int(answer)
        problem.type1 = type1
        problem.type2 = type2
        problem.difficulty = int(difficulty)
        problem.explanation = explanation
    else:
        problem = Problem(text=text, answer=int(answer), type1=type1, type2=type2, difficulty=int(difficulty), explanation=explanation).store()

    if len(unit) > 0:
        for u in unit.split(','):
            problem.unit.add(ProblemUnit.objects.get(unit=u).store())

    if len(middleUnit) > 0:
        for u in middleUnit.split(','):
            if ProblemMiddleUnit.objects.filter(middleUnit=u).exists():
                problem.middleUnit.add(ProblemMiddleUnit.objects.get(middleUnit=u).store())
            else:
                problem.middleUnit.add(ProblemMiddleUnit(middleUnit=int(u)).store())

    if len(smallUnit) > 0:
        for u in smallUnit.split(','):
            if ProblemSmallUnit.objects.filter(smallUnit=u).exists():
                problem.smallUnit.add(ProblemSmallUnit.objects.get(smallUnit=u).store())
            else:
                problem.smallUnit.add(ProblemSmallUnit(smallUnit=int(u)).store())

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
    return render(request, 'basic_info/problem.html', {'middleUnit': MIDDLE_UNIT, 'smallUnit': SMALL_UNIT})


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


def new_users(request):
    return render(request, 'consult_req/new_users.html')


def users(request):
    return render(request, 'consult_req/users.html',  {'users': User.objects.all().order_by('-createdAt')})


def id_certificate(request):
    userSrl = request.GET.get('userSrl')
    user = User.objects.get(userSrl=int(userSrl))
    user.isCardCertificate = True
    user.save()
    return returnHttpResponse({'msg': user.id + '님의 학생증 인증이 완료 되었습니다.'})

