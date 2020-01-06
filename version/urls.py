from version import views
from django.urls import path, include
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('versions/', (views.AstorologyVersionList.as_view())),
    path('versions/<int:pk>/', views.AstorologyVersionDetail.as_view()),

]
