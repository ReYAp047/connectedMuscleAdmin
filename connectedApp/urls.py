"""connectedApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from coach import views as coachViews
from member import views as memberViews
from product import views as productViews
from transformation import views as transformationViews
from programme import views as programmeViews

admin.site.site_header= "| Connected Muscles |"

urlpatterns = [
    path('admin/', admin.site.urls),
        path('Coach/', coachViews.CoachList.as_view()),
        
        path('Member/', memberViews.MemberList.as_view()),

        path('Product/', productViews.ProductList.as_view()),
        path('Category/', productViews.ProductCategoryList.as_view()),

        path('Transformation/', transformationViews.TransformationList.as_view()),

        path('Chest/', programmeViews.ChestList.as_view()),
        path('Back/', programmeViews.BackList.as_view()),
        path('Shoulders/', programmeViews.ShouldersList.as_view()),
        path('Legs/', programmeViews.LegsList.as_view()),
        path('Biceps/', programmeViews.BicepsList.as_view()),
        path('Triceps/', programmeViews.TricepsList.as_view()),
        path('Cardio/', programmeViews.CardioList.as_view()),
        path('Programme/', programmeViews.ProgrammeList.as_view()),

]



        
