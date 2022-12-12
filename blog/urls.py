from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.PostDetail.as_view()),
    path('category/<str:slug>/',views.category_page),
    # https://project-ztsct.run.goorm.io/blog/category/programming
    # programming만 떼어 views.py의 category_page()
    path('',views.PostList.as_view()),
    
]