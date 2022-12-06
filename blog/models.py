from django.db import models

# 함수를 사용하는 방법과 class를 사용하는 방법

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
        
    # author : 추후 작성 예정 
# Create your models here.
