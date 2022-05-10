"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import blog.views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- Admin ---
    path('admin/', admin.site.urls),

    # --- Authentication ---
    #path('', authentication.views.login_page, name='login'), # vue def
    #path('', authentication.views.LoginPage.as_view(), name='login'),  # vue class
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),  # Implémentation de la vue générique login

    path('logout/', LogoutView.as_view(), name='logout'),  # Implémentation de la vue générique logout
    #path('logout/', authentication.views.logout_user, name='logout'),

    path('password-change/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html',
    ), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ), name='password_change_done'),

    path('signup', authentication.views.signup_page, name='signup'),

    # --- Blog ---
    path('home/', blog.views.home, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),
]

if settings.DEBUG: # si on est dans notre environement de developpement
    # Media servis dans l'environement de developpement
    #    ( valable qu'en dev. Pour le deploiement il faudra trouver comment faire !)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
