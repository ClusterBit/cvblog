from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('about/', views.about.as_view(), name='about'),
    path('post/create/', views.create_post, name='post_create'),
    path('signup/', views.signup.as_view(), name='signup'),
    path('signup/company/', views.signup_company, name='signup_company'),
    path('signup/customer/', views.signup_customer, name='signup_customer'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
