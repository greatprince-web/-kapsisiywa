from django.urls import path, include
from church import views  # Import views from church
from rest_framework.routers import DefaultRouter
from church import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = []  # Initialize urlpatterns as an empty list
urlpatterns += router.urls
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = []  # Initialize urlpatterns as an empty list
urlpatterns += [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('member_dashboard/', views.member_dashboard, name='member_dashboard'),
    path('sermons/', views.sermons, name='sermons'),
    path('ministries/', views.ministries, name='ministries'),
    path('events/', views.events, name='events'),  # Correctly using views.events here
    path('events/', views.events, name='events'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/edit/', views.event_update, name='event_update'),
    path('give/', views.give_view, name='give'),
]
