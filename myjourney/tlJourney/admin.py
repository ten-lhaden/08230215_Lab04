from django.contrib import admin
from .models import LearningYear, Skill, Hobby, Profile

# Register models
admin.site.register(LearningYear)
admin.site.register(Skill)
admin.site.register(Hobby)
admin.site.register(Profile)
