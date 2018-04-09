import uuid
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.


class Photo(models.Model):
    photoSrl = models.AutoField(primary_key=True)
    photo = models.ImageField(max_length=300, null=True, upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo.name

    def store(self):
        self.save()
        return self

    def get_url(self):
        return str(self.photo.url).replace("https", "http")

    def get_https_url(self):
        return str(self.photo.url)

    def get_extention(self):
        return str(self.photo.url)[str(self.photo.url).rfind('.')+1:]

    def is_jpeg(self):
        return True if self.get_extention().upper() in ['JPEG', 'JPG'] else False


PROBLEM_TYPE1 = {
    (1, '내신형'),
    (2, '수능형'),
}

PROBLEM_TYPE2 = {
    (1, '개념확인형'),
    (2, '개념응용형'),
}

PROBLEM_DIFFICULTY = {
    (1, '쉬움'),
    (2, '중간'),
    (3, '어려움'),
}

UNIT = [
    (1, '수1'),
    (2, '수2'),
    (3, '미적1'),
    (4, '미적2'),
    (5, '확통'),
    (6, '기벡'),
]

ANSWER_TYPE = {
    (1, '객관식'),
    (2, '주관식'),
}


class ProblemUnit(models.Model):
    problemUnitSrl = models.AutoField(primary_key=True)
    unit = models.IntegerField(choices=UNIT, blank=True, null=True)

    def __str__(self):
        return str(self.get_unit_name())

    def store(self):
        self.save()
        return self

    def get_unit_name(self):
        unit = ''
        if self.unit == 1:
            unit = '수학1'
        elif self.unit == 2:
            unit = '수학2'
        elif self.unit == 3:
            unit = '미적분1'
        elif self.unit == 4:
            unit = '미적분2'
        elif self.unit == 5:
            unit = '확률과 통계'
        elif self.unit == 6:
            unit = '기하와 벡터'
        return unit



MIDDLE_UNIT = [
    (1, '다항식'),
    (2, '방정식과 부등식'),
    (3, '도형의 방정식'),
    (4, '집합과 명제'),
    (5, '함수'),
    (6, '수열'),
    (7, '지수와 로그'),
    (8, '수열의 극한'),
    (9, '함수의 극한'),
    (10, '다항함수의 미분법'),
    (11, '다항함수의 적분법'),
    (12, '지수함수와 로그함수'),
    (13, '삼각함수'),
    (14, '미분법'),
    (15, '적분법'),
    (16, '순열과 조합'),
    (17, '확률'),
    (18, '통계'),
    (19, '이차곡선'),
    (20, '평면벡터'),
    (21, '공간도형과 공간좌표'),
    (22, '공간벡터'),
]

GET_MIDDLE_UNIT = {
    1: MIDDLE_UNIT[:3],
    2: MIDDLE_UNIT[3:7],
    3: MIDDLE_UNIT[7:11],
    4: MIDDLE_UNIT[11:15],
    5: MIDDLE_UNIT[15:18],
    6: MIDDLE_UNIT[18:22]
}


class ProblemMiddleUnit(models.Model):
    problemMiddleUnitSrl = models.AutoField(primary_key=True)
    middleUnit = models.IntegerField(choices=MIDDLE_UNIT, blank=True, null=True)

    def __str__(self):
        return str(self.get_middleUnit_display())

    def store(self):
        self.save()
        return self


SMALL_UNIT = [
    (1, '다항식의 연산'),
    (2, '항등식과 나머지 정리'),
    (3, '인수분해'),
    (4, '복소수와 이차방정식'),
    (5, '이차방정식과 이차함수'),
    (6, '여러가지 방정식'),
    (7, '여러가지 부등식'),
    (8, '평면좌표'),
    (9, '직선의 방정식'),
    (10, '원의 방정식'),
    (11, '도형의 이동'),
    (12, '부등식의 영역'),
    (13, '집합'),
    (14, '명제'),
    (15, '절대부등식'),
    (16, '함수'),
    (17, '유리식과 유리함수'),
    (18, '무리식과 무리함수'),
    (19, '등차수열과 등비수열'),
    (20, '여러가지 수열'),
    (21, '지수와 로그'),
    (22, '상용로그'),
    (23, '수열의 극한'),
    (24, '급수'),
    (25, '함수의 극한'),
    (26, '함수의 연속'),
    (27, '미분계수와 도함수'),
    (28, '도함수의 활용'),
    (29, '부정적분'),
    (30, '정적분'),
    (31, '정적분의 활용'),
    (32, '지수함수와 로그함수의 뜻과 그래프'),
    (33, '지수함수와 로그함수의 미분'),
    (34, '삼각함수의 뜻'),
    (35, '삼각함수의 그래프'),
    (36, '삼각함수의 미분'),
    (37, '여러가지 함수의 미분법'),
    (38, '도함수의 활용'),
    (39, '여러가지 함수의 적분법'),
    (40, '정적분의 활용'),
    (41, '경우의 수'),
    (42, '순열과 조합'),
    (43, '이항정리'),
    (44, '확률의 뜻'),
    (45, '조건부 확률'),
    (46, '확률변수와 확률분포'),
    (47, '통계적 추정'),
    (48, '이차곡선의 방정식'),
    (49, '이차곡선과 접선의 방정식'),
    (50, '평면벡터의 뜻'),
    (51, '평면운동'),
    (52, '공간도형'),
    (53, '공간좌표'),
    (54, '공간벡터'),
]

GET_SMALL_UNIT = {
    1: SMALL_UNIT[:3],
    2: SMALL_UNIT[3:7],
    3: SMALL_UNIT[7:12],
    4: SMALL_UNIT[12:15],
    5: SMALL_UNIT[15:18],
    6: SMALL_UNIT[18:20],
    7: SMALL_UNIT[20:22],
    8: SMALL_UNIT[22:24],
    9: SMALL_UNIT[24:26],
    10: SMALL_UNIT[26:28],
    11: SMALL_UNIT[28:31],
    12: SMALL_UNIT[31:33],
    13: SMALL_UNIT[33:36],
    14: SMALL_UNIT[36:38],
    15: SMALL_UNIT[38:40],
    16: SMALL_UNIT[40:43],
    17: SMALL_UNIT[43:45],
    18: SMALL_UNIT[45:47],
    19: SMALL_UNIT[47:49],
    20: SMALL_UNIT[49:51],
    21: SMALL_UNIT[51:53],
    22: SMALL_UNIT[53:54],
}


class ProblemSmallUnit(models.Model):
    problemSmallUnitSrl = models.AutoField(primary_key=True)
    smallUnit = models.IntegerField(choices=SMALL_UNIT, blank=True, null=True)

    def __str__(self):
        return str(self.get_smallUnit_display())

    def store(self):
        self.save()
        return self


class Problem(models.Model):
    problemSrl = models.AutoField(primary_key=True)
    text = models.CharField(max_length=2000, blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, null=True)
    answer = models.IntegerField(blank=True, null=True)

    type1 = models.IntegerField(choices=PROBLEM_TYPE1, blank=True, null=True)
    type2 = models.IntegerField(choices=PROBLEM_TYPE2, blank=True, null=True)
    difficulty = models.IntegerField(choices=PROBLEM_DIFFICULTY, blank=True, null=True)
    unit = models.ManyToManyField(ProblemUnit, blank=True, null=True)
    middleUnit = models.ManyToManyField(ProblemMiddleUnit, blank=True, null=True)
    smallUnit = models.ManyToManyField(ProblemSmallUnit, blank=True, null=True)

    answerType = models.IntegerField(choices=ANSWER_TYPE, blank=True, null=True, default=1)

    explanation = models.TextField(max_length=10000, blank=True, null=True)

    totalAnswered = models.IntegerField(default=0)
    rightAnswered = models.IntegerField(default=0)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)

    def store(self):
        self.save()
        return self

    def get_units(self):
        return list(map(lambda x: x['unit'], self.unit.values('unit')))

    def get_right_answer_percent(self):
        return int(100 * self.rightAnswered / self.totalAnswered)


TEST_TYPE = {
    (1, '일반'),
    (2, '진단고사'),
    (3, '추천고사'),
}


class Score(models.Model):
    scoreSrl = models.AutoField(primary_key=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score)

    def store(self):
        self.save()
        return self


class Test(models.Model):
    testSrl = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    type = models.IntegerField(choices=TEST_TYPE, blank=True, null=True)
    problems = models.ManyToManyField(Problem, blank=True, null=True)
    scores = models.ManyToManyField(Score, blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.testSrl)

    def store(self):
        self.save()
        return self

    def get_problem_len(self):
        return self.problems.count()

    def get_create_at(self):
        return self.createdAt.strptime('%Y %m월 %d일')


class AnswerNum(models.Model):
    answerNumSrl = models.AutoField(primary_key=True)
    answer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.answer)

    def store(self):
        self.save()
        return self


class Answer(models.Model):
    answerSrl = models.AutoField(primary_key=True)

    answers = models.ManyToManyField(AnswerNum, blank=True, null=True, related_name='answers')
    test = models.ForeignKey(Test, blank=False, null=False, on_delete=models.CASCADE)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.answerSrl)

    def store(self):
        self.save()
        return self

    def get_created_at(self):
        return self.createdAt.strftime("%Y년 %m월 %d일")

    def get_created_at_dot(self):
        return self.createdAt.strftime("%Y. %m. %d")


class Lecture(models.Model):
    lectureSrl = models.AutoField(primary_key=True)
    video = models.FileField(max_length=300, null=True, upload_to='videos/')
    unit = models.ManyToManyField(ProblemUnit, null=True, blank=True)
    middleUnit = models.ManyToManyField(ProblemMiddleUnit, null=True, blank=True)
    teacherName = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.video)

    def store(self):
        self.save()
        return self

    def get_url(self):
        return str(self.video.url).replace("https", "http")

    def get_https_url(self):
        return str(self.video.url)


GRADE = {
    (1, '1학년'),
    (2, '2학년'),
    (3, '3학년'),
}


class StudyDate(models.Model):
    studyDateSrl = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    smallUnit = models.ForeignKey(ProblemSmallUnit, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

    def store(self):
        self.save()
        return self


class Recommend(models.Model):
    recommendSrl = models.AutoField(primary_key=True)
    aimGrade = models.IntegerField(blank=True, null=True)
    unit = models.ForeignKey(ProblemUnit, blank=True, null=True, on_delete=models.CASCADE)
    studyDate = models.ManyToManyField(StudyDate, blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.recommendSrl)

    def store(self):
        self.save()
        return self

    def get_problem_count(self):
        return Problem.objects.filter(unit=self.unit).count()

    def get_lecture_count(self):
        return Lecture.objects.filter(unit=self.unit).count()


class User(models.Model):
    userSrl = models.AutoField(primary_key=True)
    id = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    grade = models.IntegerField(choices=GRADE, blank=True, null=True)
    idCard = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.CASCADE)

    answers = models.ManyToManyField(Answer, blank=True, null=True)
    recommend = models.ManyToManyField(Recommend, blank=True, null=True)
    tests = models.ManyToManyField(Test, blank=True, null=True)

    isCardCertificate = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    def store(self):
        self.save()
        return self

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        self.save()

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def get_last_answer(self):
        return self.answers.last()

    def get_answers(self):
        return self.answers.filter(test__type=2)

    def get_created_at(self):
        return self.createdAt.strftime("%Y-%m-%d %H:%M")


BOARD_TYPE = {
    (1, '소식'),
    (2, '칼럼'),
    (3, '커뮤니티')
}


class Comment(models.Model):
    commentSrl = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000, null=True, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def store(self):
        self.save()
        return self

    def get_write_time(self):
        return self.createdAt.strftime('%Y. %m. %d %H:%M')


class Board(models.Model):
    boardSrl = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(max_length=10000, null=True, blank=True)
    writer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    viewCnt = models.IntegerField(null=True, blank=True, default=0)
    recommendCnt = models.IntegerField(null=True, blank=True, default=0)
    type = models.IntegerField(choices=BOARD_TYPE, null=True, blank=True)

    comments = models.ManyToManyField(Comment, null=True, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def store(self):
        self.save()
        return self

    def get_write_day(self):
        return self.createdAt.time() if self.createdAt.date() == datetime.today().date() else str((datetime.today().date() - self.createdAt.date()).days) + ' 일전'

    def get_write_time(self):
        return self.createdAt.strftime('%Y. %m. %d %H:%M')

    def get_comment_len(self):
        return self.comments.count()


class Rating(models.Model):
    ratingSrl = models.AutoField(primary_key=True)

    su1 = models.IntegerField(blank=True, null=True)
    su2 = models.IntegerField(blank=True, null=True)
    mi1 = models.IntegerField(blank=True, null=True)
    mi2 = models.IntegerField(blank=True, null=True)
    givec = models.IntegerField(blank=True, null=True)
    hwaktong = models.IntegerField(blank=True, null=True)

    score = models.IntegerField(default=0)
    totalScore = models.IntegerField(default=0)

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, blank=True, null=True, on_delete=models.CASCADE)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ratingSrl)

    def store(self):
        self.save()
        return self

    def get_updated_at(self):
        return self.updatedAt.strftime("%Y. %m. %d")

    def get_grade(self):
        return str(int((self.su1 + self.su2 + self.mi1 + self.mi2 + self.givec + self.hwaktong) / 6))
