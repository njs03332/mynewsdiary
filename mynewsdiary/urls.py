"""mynewsdiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newsdiary import views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.temp, name='temp'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
	path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article'),
    path('preview/', views.PreviewView.as_view(), name='preview'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('follow/<int:pk>/', views.follow, name='follow'),
    path('unfollow/<int:pk>/', views.unfollow, name='unfollow'),

]
