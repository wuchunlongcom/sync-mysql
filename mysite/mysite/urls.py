from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    
    
    url(r'^', include('account.urls')),
    #url(r'^$', RedirectView.as_view(url='/account/index/', query_string=True)),
    #url(r'^$', RedirectView.as_view(url='/login/', query_string=True)),
]
