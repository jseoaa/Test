from django.urls import path
from . import views 

urlpatterns = [ 
    # path('',views.index),
    # #는 views.py 의 index 함수를 PostList 클래스로 대체해서 주석
    #/blog 뒤에 아무것도 안붙이면 여기로 넘어옴
    path('', views.PostList.as_view()),
    # PostList 를 쓰면 
    # template 로 갈땐 post_list.html으로 간다 
    

    path('<int:pk>/', views.PostDetail.as_view())
    
]