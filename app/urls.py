from django.urls import path
from.views import (HomePageView, AboutPageView, AlertListView,
                   AlertDetailView, AlertCreateView, AlertUpdateView,
                   AlertDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('alert/', AlertListView.as_view(), name='alert'),
    path('alerts/', AlertListView.as_view(), name='alert_list'),
    path('alert/<int:pk>/', AlertDetailView.as_view(), name='alert_detail'),
    path('alert/create/', AlertCreateView.as_view(), name='alert_create'),
    path('alert/<int:pk>/edit/', AlertUpdateView.as_view(), name='alert_update'),
    path('alert/<int:pk>/delete/', AlertDeleteView.as_view(), name='alert_delete'),
]
