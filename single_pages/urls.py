from django.urls import path 
from . import views

urlpatterns = [
    path('<int:pk>/',views,PostDetail.as.view()),
    # path('about_me/',views.about_me),
    path('',views.PostList.as.view()),
    
]