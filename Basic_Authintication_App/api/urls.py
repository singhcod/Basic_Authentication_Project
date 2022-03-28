from django.urls import path,include
from Basic_Authintication_App.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee',views.Employee_Model_View)

urlpatterns =[
    path('',include(router.urls)),
]