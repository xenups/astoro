from feedback import views
from django.urls import path, include
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('feedbacks/', (views.FeedBackList.as_view())),

]
