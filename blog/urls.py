from django.urls import path,include
from blog import views
urlpatterns = [
  path('' ,views.home , name="bloghome"),
  path('test' , views.search , name="test"),
  path('<str:slug>' , views.postDetail, name="blogdetail"),
  path('catagory/<str:catagory>' , views.CatagoryWise , name="catagorywise"),
]