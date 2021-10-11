from django.contrib import admin
from django.urls import path
# from .views import StudentView
# from . import views
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
]
    