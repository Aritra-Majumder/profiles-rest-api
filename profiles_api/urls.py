from django.urls import path,include
#for viewsets
from rest_framework.routers import DefaultRouter 

from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)



urlpatterns = [
    path('helloApiView/', views.HelloAPIView.as_view(), name='test'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('',include(router.urls)),
]
