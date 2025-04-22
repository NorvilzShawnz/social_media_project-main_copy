from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
    path('view-post/', views.view_post, name='view-post'),
    path('find-groups/', views.find_groups, name='find-groups'),
    path('group-page/', views.group_page, name='group-page'),
    path('find-users/', views.find_users, name='find-users'),
]
