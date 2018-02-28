#!/bin/bash

python3.5 manage.py makemigrations math_problem math_problem_app math_admin
python3.5 manage.py migrate

