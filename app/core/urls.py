from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup.as_view(), name='signup'),
    path('signup/company/', views.signup_company, name='signup_company'),
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('post/list/', views.post_list, name='post_list'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='post_create'),
    path('news/list', views.news_list, name='news_list'),
    path('news/<slug:slug>', views.news_detail, name='news_detail'),
    path('catalog/', views.catalog_list, name='catalog_list'),
    path('catalog/<int:pk>', views.catalog_detail, name='catalog_detail'),
    path('about/', views.about.as_view(), name='about'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
