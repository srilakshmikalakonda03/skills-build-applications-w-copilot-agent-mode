"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root
from django.http import JsonResponse


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

def api_root_with_codespace(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    api_base = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({
        "message": "Welcome to the Octofit Tracker API!",
        "api_base": api_base,
        "example_activities_url": api_base + "activities/",
        "note": "Replace $CODESPACE_NAME with your actual codespace name if running locally."
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root_with_codespace, name='api-root'),
    path('api/activities/', ActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='activity-list'),
    path('api/activities/<int:pk>/', ActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='activity-detail'),
    path('api/teams/', TeamViewSet.as_view({'get': 'list', 'post': 'create'}), name='team-list'),
    path('api/teams/<int:pk>/', TeamViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='team-detail'),
    path('api/users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('api/users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    path('api/workouts/', WorkoutViewSet.as_view({'get': 'list', 'post': 'create'}), name='workout-list'),
    path('api/workouts/<int:pk>/', WorkoutViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='workout-detail'),
    path('api/leaderboard/', LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard-list'),
]
"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

