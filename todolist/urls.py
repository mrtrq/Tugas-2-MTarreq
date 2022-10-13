
from django.urls import path
#from symbol import parameters
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import *

app_name = 'todolist'
urlpatterns = [
    path('',show_todolist, name='show_todolist'),
    path('register/',register, name='register'),
    path('login/',login_user, name='login_user'),
    path('logout/',logout_user, name='logout_user'),
    path('create-task/',create_task, name='create_task'),
    path('update-task/<int:i>/',update_task, name='update_task'),
    path('delete-task/<int:i>/',delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('show-ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('post-ajax', post_ajax_todolist, name='post_ajax_todolist'),
]