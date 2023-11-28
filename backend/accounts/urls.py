from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'
urlpatterns = [
    path('signup/', include("dj_rest_auth.registration.urls")),
    path('', include("dj_rest_auth.urls")),
    # path('signup/', views.signup, name='signup'),
    # path('api-token-auth/', obtain_jwt_token, name='api-token-auth'),
    path('info/', views.info, name='info'),
    path('profile/', views.profile, name='profile'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
]