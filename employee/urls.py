from django.urls import path

from .views import ArticleView


# to help us do a reverse look-up latter
APP_NAME = "employee"


# 2nd path to update employee fields
urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:pk>', EmployeeView.as_view())
]