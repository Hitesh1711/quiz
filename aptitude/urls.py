from django.urls import path

from . import views

urlpatterns = [
    path('', views.category),
    path('category/<str:subcatname>', views.question),
    path('<str:catname>', views.sub_category),
    path('category/aptitude/discussion/<int:qid>', views.discussion),
    path('category/aptitude/discussion/<int:qid>', views.discussion),
    path('aboutus/', views.aboutus),
]
