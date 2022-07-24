from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ProjectView
router = DefaultRouter()
router.register('details/',ProjectView)


urlpatterns = [path('',include(router.urls))]
