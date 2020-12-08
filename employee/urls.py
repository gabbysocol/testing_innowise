from django.urls import path

from .views import ArticleView


# to help us do a reverse look-up latter
APP_NAME = "employee"


urlpatterns = [
    path('employee/', EmployeeView.as_view()),
]