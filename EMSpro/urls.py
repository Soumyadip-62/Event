from django.contrib import admin
from django.urls import path, include
from baseApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',views.base,name='base'),
    path('album/', views.Album,name='album'),
    path('admin/', admin.site.urls),
    path('Wedding/', views.Wedding,name='Wedding'),
 	path('Wedding/', include('baseApp.urls'),name='Wedding'),
    path('Birthday/', views.Birthday,name='Birthday'),
    path('accounts/',include('accounts.urls')),
    path('anniversary/', views.Anniversary,name='anniversary'),
 	path('anniversary/', include('baseApp.urls'),name='anniversary'),
	path('makeuppage',views.makeuppage,name='makeuppage'),
	path('venuepage/',views.venuepage,name='venuepage'),
	path('venuepageANNI/',views.venuepageANNI,name='venuepageANNI'),
    path('venuebpage/',views.venuebpage,name='venuebpage'),
    path('cateringpage/',views.cateringpage,name='cateringpage'),
    path('cateringpageBIRTHDAY/',views.cateringpageBIRTHDAY,name='cateringpageBIRTHDAY'),
    path('cateringpageANNI/',views.cateringpageANNI,name='cateringpageANNI'),
	path('special_celebration/',views.Special_celebration,name='special_celebration'),
	path('anniversary_theme/',views.anniversary_theme,name='anniversary_theme'),
	path('admindashboard/',views.admindashboard,name='admindashboard'),
	path('viewrequest/',views.user_request_status,name='viewrequest'),
	path('newmakup/',views.new_makup,name='newmakup'),
	path('packages/',views.bpackage,name='packages'),
	path('weddingpackages/',views.wpackage,name='weddingpackages'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
