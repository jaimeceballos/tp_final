from django.conf.urls import include, url
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
   url(r'^$', auth_views.login, {'template_name': 'login.html'},name='login'),
   url(r'^logout/$',logout,name='logout'),
   url(r'^password/reset/$','django.contrib.auth.views.password_reset',{'post_reset_redirect' : '/usuarios/password/reset/done/', 'template_name' : 'password_reset.html','email_template_name':'password_reset_email.html'},name="password_reset"),
   url(r'^password/reset/done/$','django.contrib.auth.views.password_reset_done',{'template_name':'password_reset_done.html'}),
   url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm',{'post_reset_redirect' : '/usuarios/password/done/','template_name':'confirm.html'}),
   url(r'^password/done/$','django.contrib.auth.views.password_reset_complete',{'template_name':'finalizado.html'}),
   url(r'^registro/$',registro,name='registro'),
   url(r'^confirmar/(?P<activation_key>\w+)/$',confirmar,name='confirmar'),
   url(r'^password-change/$',auth_views.password_change,{'template_name': 'password-change.html','post_change_redirect':'login'}),
   url(r'^editar_perfil/$',editar_perfil,name='editar_perfil'),
   url(r'^admin/', include(admin.site.urls)),
]