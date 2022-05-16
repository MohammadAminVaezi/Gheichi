from django.urls import path
from .views import UrlListView, UrlCreateView, UrlRedirectView, UrlCopyPathView, UrlEditPathView, RedirectPage

app_name = 'scissors'
urlpatterns = [
    path('', UrlListView.as_view(), name='list-url'),
    path('url/', UrlCreateView.as_view(), name='create-url'),
    path('s/<str:path>/', UrlRedirectView.as_view(), name='redirect-url'),
    path('copy/<int:pk>/', UrlCopyPathView.as_view(), name='copy-url'),
    path('<int:pk>/', UrlEditPathView.as_view(), name='edit-url'),
    path('about_us/', RedirectPage.as_view(), name='redirect-page'),


]
