from django.urls import path
from blog import views
urlpatterns = [
    path('',views.index,name='bloghome'),
    path('blogpost/', views.blogpost, name="blogHome"),
]
