from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from church import views  
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('api/welcome/', views.welcome_data, name='welcome-data'),
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('member_dashboard/', views.member_dashboard, name='member_dashboard'),
    path('sermons/', views.sermons, name='sermons'),
    path('ministries/', views.ministries, name='ministries'),
    path('events/', views.events, name='events'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/edit/', views.event_update, name='event_update'),
    path('give/', views.give_view, name='give'),
]

# Only in development: Serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
