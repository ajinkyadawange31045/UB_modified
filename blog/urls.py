from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post,category,user_signup, user_login, user_logout


urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
]
