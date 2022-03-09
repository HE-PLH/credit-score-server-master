from django.conf.urls import url
from CreditScore import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^score', views.ScoreApi),
    url(r'^farmer$', views.FarmerApi),
    url(r'^farmer/([0-9]+)$', views.FarmerApi),
    url(r'^farm$', views.FarmApi),
    url(r'^farm/([0-9]+)$', views.FarmApi),
    url(r'^_farm$', views.FaarmApi),
    url(r'^_farm/([0-9]+)$', views.FaarmApi),
    url(r'^finance$', views.FinanceApi),
    url(r'^finance/([0-9]+)$', views.FinanceApi),
    url(r'^weather', views.WeatherApi),
    url(r'^weather/([0-9]+)$', views.WeatherApi),
    url(r'^social-interaction', views.SocialInteractionApi),
    url(r'^social-interaction/([0-9]+)$', views.SocialInteractionApi),
    url(r'^psychometric-assessment', views.PsychometricAssessmentApi),
    url(r'^psychometric-assessment/([0-9]+)$', views.PsychometricAssessmentApi),
    url(r'^question-category', views.QuestionCategoryApi),
    url(r'^question-category/([0-9]+)$', views.QuestionCategoryApi),
    url(r'^question-type', views.QuestionTypeApi),
    url(r'^question-type/([0-9]+)$', views.QuestionTypeApi),
    url(r'^question-answer', views.QuestionAnswerApi),
    url(r'^question-answer/([0-9]+)$', views.QuestionAnswerApi),
]
