from django.urls import path
from Blooby.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:username>/', profile, name='profile'),
    path('editar/', editar, name='editar'),
    path('register/', register, name='register'),
	path('login/', LoginView.as_view(template_name='Blooby/login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('delete/<int:post_id>/', delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)