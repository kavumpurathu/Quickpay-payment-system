from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('indexadmin/', views.indexadmin, name='indexadmin'),
    path('adminuserview/', views.adminuserview, name='adminuserview'),
    path('usetpwd/', views.usetpwd, name='usetpwd'),
    path('usetpwd1/', views.usetpwd1, name='usetpwd1'),
    path('deleteuser/<str:uname>', views.deleteuser, name='deleteuser'),
    path('reactivateuser/<str:uname>', views.reactivateuser, name='reactivateuser'),
    path('reactivatesp/<str:uname>', views.reactivatesp, name='reactivatesp'),
    path('adminspview/', views.adminspview, name='adminspview'),
    path('deletesp/<str:uname>', views.deletesp, name='deletesp'),
    path('admindth/', views.admindth, name='admindth'),
    path('adminmob/', views.adminmob, name='adminmob'),
    path('admincmpl/', views.admincmpl, name='admincmpl'),
    path('deletecmpl/<int:id>', views.deletecmpl, name='deletecmpl'),
    # path('deactivateuser/', views.deactivateuser, name='deactivateuser'),
    # path('activateuser/<int:id>',views.activateuser, name='activateuser'),
    path('user_reg/', views.user_reg, name='user_reg'),
    path('login/', views.login, name='home_login'),
    path('logincheck/', views.logincheck, name='home_logincheck'),
    path('services/', views.services, name='home_services'),
    path('comreply/<str:uname>', views.comreply, name='comreply'),
    path('vwcomplaints/', views.vwcomplaints, name='vwcomplaints'),
    path('aboutus/', views.aboutus, name='home_about'),
    path('care/', views.care, name='user_care'),
    path('care1/', views.care1, name='user_care1'),
    path('dcharge/', views.dcharge, name='user_dcharge'),
    path('dcharge1/', views.dcharge1, name='user_dcharge1'),
    path('mcharge/', views.mcharge, name='user_mcharge'),
    path('mobofr/<str:sname>', views.mobofr, name='mobofr'),
    path('vwoffer_user/<str:sp>', views.vwoffer_user, name='vwoffer_user'),
    path('viewoffer/', views.viewoffer, name='viewoffer'),
    path('viewoffer1/', views.viewoffer1, name='viewoffer1'),
    path('mcharge1/', views.mcharge1, name='user_mcharge1'),
    path('payment/', views.payment, name='user_payment'),
    path('paynow/',views.paynow, name='user_paynow'),
    path('sphome/',views.sphome, name='sp_home'),
    path('signup/',views.signup, name='signup'),
    path('spsignup/',views.spsignup, name='spsignup'),
    path('spregister/',views.spregister, name='sp_register'),
    path('spdtls/<str:spuname>',views.spdtls, name='spdtls'),
    path('ofrsave/',views.ofrsave, name='ofrsave'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('rehistory/<str:uname>',views.rehistory, name='re_history'),
    path('rerequest/<str:suname>/<str:spname>',views.rerequest, name='rerequest'),
    path('serviceprofile/<str:spuname>',views.serviceprofile, name='serviceprofile'),
    path('spsave/<str:suname>',views.spsave, name='spsave'),
    # path('reply/<str:spuname>/<str:spname>',views.reply,name='reply'),
    path('spreply/<str:spname>',views.spreply,name='spreply'),
    # path('spreplydemo/<str:spname>',views.spreplydemo,name='spreplydemo'),
    path('newfun/<int:id>',views.newfun, name='newfun'),
    # path('newfun1/<str:uname>',views.newfun1, name='newfun1'),
    path('complaintsave/<int:id>/<str:spname>',views.complaintsave, name='complaintsave'),
    path('complaintvw/',views.complaintvw, name='complaintvw'),
    path('comview/<str:spname>',views.comview, name='comview'),
    # path('demo/<str:spname>',views.demo, name='demo'),
    path('userhome/',views.userhome, name='user_home'),
    path('wallt/',views.wallt,name='wallt'),
    path('dthsum/',views.dthsum,name='dthsum'),
    path('mobsum/',views.mobsum,name='mobsum'),
    path('vwoffer/<str:spname>/<str:sname>',views.vwoffer, name='vwoffer'),
    path('vwoffer1/',views.vwoffer1, name='vwoffer1'),
    path('rechargepay/',views.rechargepay, name='rechargepay'),
    path('rechargepaywal/',views.rechargepaywal,name='rechargepaywal'),
    path('billfun/<int:id>/<str:fname>/<str:s_provider>/<str:category>/<str:service_no>/<str:amount>/<str:date>',views.billfun, name='billfun'),
    path('logout/',views.logout, name='logout') 


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

