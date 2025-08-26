"""
URL configuration for Activity2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from History.models import History
from History.views import history_list
from Tweets.views import home, TweetListView, TweetCreateView, HistoryListView
from accounts.views import register, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('<int:id/', TweetDetailView.as_view(), name='detail_view'),
    path('tweets/', TweetListView.as_view(), name='list_view'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('history/', HistoryListView.as_view(), name='history_list'),
]
