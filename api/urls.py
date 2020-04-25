from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Index, CreateUser, ListUsers, DeleteUser

urlpatterns = [
    url(r'^api/exercise/log/?$', Index.as_view()),
    url(r'^api/exercise/new-user/?$', CreateUser.as_view()),
    url(r'^api/exercise/users/?$', ListUsers.as_view()),
    path('api/exercise/users/delete/<int:pk>/', DeleteUser.as_view())
]


