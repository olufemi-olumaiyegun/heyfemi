from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<int:post_id>',views.content, name='content'),
    path('categories/<int:category_id>', views.category, name='categories')
]
