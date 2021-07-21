from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Wedding,name='wedding'),
    path('',views.Anniversary,name='anniversary'),
	path('makeuppage/',views.makeuppage,name='makeuppage'),
    path('venuepage/',views.venuepage,name='venuepage'),
    path('venuepageANNI/',views.venuepageANNI,name='venuepageANNI'),
    path('venuebpage/',views.venuebpage,name='venuebpage'),
    path('cateringpage/',views.cateringpage,name='cateringpage'),
    path('cateringpageBIRTHDAY/',views.cateringpageBIRTHDAY,name='cateringpageBIRTHDAY'),
    path('cateringpageANNI/',views.cateringpageANNI,name='cateringpageANNI'),
    path('viewrequest/',views.user_request_status,name='viewrequest'),
   	path('special_celebration/',views.Special_celebration,name='special_celebration'),
	path('anniversary_theme/',views.anniversary_theme,name='anniversary_theme'),
    path('packages/',views.bpackage,name='packages'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
