"""django_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from users.views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^', include('loginapp.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    # url(r'^signup/$', CreateView.as_view(template_name='register.html', form_class=UserCreationForm,
    #                                      success_url='/')),
    url(r'^register/$', register, name='register'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls))
#     ]
