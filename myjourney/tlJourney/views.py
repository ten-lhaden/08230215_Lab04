from django.shortcuts import render
from .models import Hobby, LearningYear, Skill

def index(request):
    learning_years = LearningYear.objects.all()
    skills = Skill.objects.all()

    context = {
        'learning_years': learning_years,
        'skills': skills,
    }

    return render(request, 'index.html', context)


def about_me(request):
    hobbies = Hobby.objects.all()

    context = {
        'hobbies': hobbies,
    }

    return render(request, 'aboutMe.html', context)
