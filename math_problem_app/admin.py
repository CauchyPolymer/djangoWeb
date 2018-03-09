from django.contrib import admin

# Register your models here.
from math_problem_app.models import User, Rating, ProblemUnit, Problem

admin.site.register(User)
admin.site.register(Rating)
admin.site.register(ProblemUnit)
admin.site.register(Problem)