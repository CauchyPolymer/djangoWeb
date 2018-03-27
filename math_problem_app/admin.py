from django.contrib import admin

# Register your models here.
from math_problem_app.models import *

admin.site.register(User)
admin.site.register(Rating)
admin.site.register(ProblemUnit)
admin.site.register(Problem)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(AnswerNum)
admin.site.register(Score)

admin.site.register(ProblemMiddleUnit)
admin.site.register(ProblemSmallUnit)