from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # '<slug:slug>/' below = django slug path converter and slug in PostDetail
    # get method
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
