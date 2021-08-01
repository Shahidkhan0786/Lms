from django.urls import path

from course import views
urlpatterns = [
    path('', views.home),
    path('courses' , views.courses , name="allcourses"),
    path('course/<str:slug>' , views.coursePage , name="coursepage"),
    path('about',views.about ,name="about"),
    path('snd',views.mailsnd , name="contactmail"),
    path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/")),
    path('profile/<int:pk>', views.MyProfileDetailView.as_view()),


]
