from django.contrib import admin
from .models import Farmer, Farm, Finance, Weather, SocialInteraction, PsychometricAssessment, QuestionAnswer, \
    QuestionType, QuestionCategory

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Farm)
admin.site.register(Finance)
admin.site.register(Weather)
admin.site.register(SocialInteraction)
admin.site.register(PsychometricAssessment)
admin.site.register(QuestionCategory)
admin.site.register(QuestionType)
admin.site.register(QuestionAnswer)
