import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.


class Rating(models.Model):
    ratingSrl = models.AutoField(primary_key=True)

    su1 = models.IntegerField(blank=True, null=True)
    su2 = models.IntegerField(blank=True, null=True)
    mi1 = models.IntegerField(blank=True, null=True)
    mi2 = models.IntegerField(blank=True, null=True)
    givec = models.IntegerField(blank=True, null=True)
    hwaktong = models.IntegerField(blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ratingSrl)

    def store(self):
        self.save()
        return self

    def get_updated_at(self):
        return self.updatedAt.strftime("%Y. %m. %d")


class Photo(models.Model):
    photoSrl = models.AutoField(primary_key=True)
    photo = models.ImageField(max_length=200, null=True,
                              upload_to='resource/photos/'+str(uuid.uuid4()))
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


PROBLEM_TYPE = {
    (1, '내신형'),
    (2, '수능형'),
    (3, '개념확인형'),
    (4, '개념응용형'),
}

PROBLEM_DIFFICULTY = {
    (1, '쉬움'),
    (2, '중간'),
    (3, '어려움'),
}

UNIT = {
    (1, '수1'),
    (2, '수2'),
    (3, '미적1'),
    (4, '미적2'),
}


class ProblemUnit(models.Model):
    problemUnitSrl = models.AutoField(primary_key=True)
    unit = models.IntegerField(choices=UNIT, blank=True, null=True)

    def __str__(self):
        return str(self.get_unit_display())


class Problem(models.Model):
    problemSrl = models.AutoField(primary_key=True)
    value = models.CharField(max_length=2000, blank=True, null=True)
    photo1 = models.ForeignKey(Photo, related_name='photo1', blank=True, null=True, on_delete=models.CASCADE)
    photo2 = models.ForeignKey(Photo, related_name='photo2', blank=True, null=True,  on_delete=models.CASCADE)
    answer = models.IntegerField(blank=True, null=True)

    type = models.IntegerField(choices=PROBLEM_TYPE, blank=True, null=True)
    difficulty = models.IntegerField(choices=PROBLEM_DIFFICULTY, blank=True, null=True)
    unit = models.ManyToManyField(ProblemUnit, blank=True, null=True)


    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.value)

    def store(self):
        self.save()
        return self


class Test(models.Model):
    testSrl = models.AutoField(primary_key=True)

    problems = models.ManyToManyField(Problem, blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.testSrl)

    def store(self):
        self.save()
        return self


class Answer(models.Model):
    answerSrl = models.AutoField(primary_key=True)
    a1 = models.IntegerField(blank=True, null=True)
    a2 = models.IntegerField(blank=True, null=True)
    a3 = models.IntegerField(blank=True, null=True)
    a4 = models.IntegerField(blank=True, null=True)
    a5 = models.IntegerField(blank=True, null=True)
    a6 = models.IntegerField(blank=True, null=True)
    a7 = models.IntegerField(blank=True, null=True)

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


class User(models.Model):
    userSrl = models.AutoField(primary_key=True)
    id = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)

    rate = models.ForeignKey(Rating, blank=True, null=True, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer, blank=True, null=True)

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


