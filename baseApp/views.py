from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import MakeupArtist,CateringService,VenueManagement,VenuebbManagement,BookingManagement,ServiceFor,BookingStatus,AnniSpecial,AnniTheme,AnniPics,BirthdayPics,WeddPics,PackageManagement,Contact
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from baseApp.forms import FormBookingStatus,FormNewMakeupArtist
from datetime import date


# Create your views here.
def base(request):

	if request.method=="POST":
		contact=Contact()
		name=request.POST.get('name')
		email=request.POST.get('email')
		feedbacks=request.POST.get('feedbacks')
		contact.name=name
		contact.email=email
		contact.feedbacks=feedbacks
		contact.save()
		# return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")
		
	return render (request,'base.html')

def Album(request):
  wp= WeddPics.objects.all()
  ap= AnniPics.objects.all()
  bp= BirthdayPics.objects.all()


  return render (request,'album.html',{'pic':wp,'pic1':ap,'pic2':bp,})

def Wedding(request):
	cs= CateringService.objects.all()[:3]
	ma_data= MakeupArtist.objects.all()[:3]
	venue= VenueManagement.objects.all().order_by('venue_type').distinct()[:3]
	wp= WeddPics.objects.all()[:3]
	pkg=PackageManagement.objects.all().filter(event_type='Marriage')[:3]
	return render(request,'Wedding.html',{'CatSer':cs,'makeup_artist':ma_data,'venues':venue,'pic1':wp,'Pack':pkg})

# @login_required(login_url='login')
# refer this for venuepage funcation
def makeuppage (request):
	ma_data= MakeupArtist.objects.all()
	if request.method=="POST":
		mua_id = request.POST["mua_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='makeup artist')
		mua=MakeupArtist.objects.get(pk=mua_id)
		reguest_for= mua.mua_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=mua.mua_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()

		HttpResponseRedirect("Wedding/")

	return render(request,'makeup_details.html',{'MAData':ma_data})

def Birthday(request):
	cs= CateringService.objects.all()[:3]
	venueb= VenuebbManagement.objects.all().order_by('venueb_type').distinct()[:3]
	bp= BirthdayPics.objects.all()[:3]
	pkg=PackageManagement.objects.all().filter(event_type='Birthday')[:3]
	return render(request,'Birthday.html',{'CatSer':cs,'venuebs':venueb,'pic2':bp,'Pack':pkg})

def Anniversary(request):
	cs= CateringService.objects.all()[:3]
	an = AnniSpecial.objects.all()[:3]
	anni_thm = AnniTheme.objects.all()[:3]
	annip= AnniPics.objects.all()[:3]
	venue= VenueManagement.objects.all().filter(venue_type='Party Hall')[:3]
	pkg=PackageManagement.objects.all().filter(event_type='Anniversary')[:3]
	return render (request, 'anniversary.html',{'an':an,'thm':anni_thm,'pic1':annip,'CSData':cs,'venues':venue,'Pack':pkg})

def Special_celebration (request):
	an= AnniSpecial.objects.all()
	if request.method=="POST":
		id = request.POST["id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='special celebration')
		sp=AnniSpecial.objects.get(pk=id)
		reguest_for= sp.arrengement_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=sp.location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		messages.success(request, 'Request have been submitted Successfully!')
		HttpResponseRedirect("Anniversary/")

	return render(request,'special_celebration.html',{'an':an})

def anniversary_theme (request):
	thm= AnniTheme.objects.all()
	if request.method=="POST":
		id = request.POST["id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='Theme_Decor')
		thm1=AnniTheme.objects.get(pk=id)
		reguest_for= thm1.theme_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,)
		booking_request.save()
		messages.success(request, 'Request have been submitted Successfully!')
		HttpResponseRedirect("Anniversary/")

	return render(request,'anniversary_theme.html',{'thm':thm})

def venuepage(request):
	vm_data= VenueManagement.objects.all()[:6]
	if request.method=="POST":
		venue_id = request.POST["venue_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='venue')
		venue=VenueManagement.objects.get(pk=venue_id)
		reguest_for= venue.venue_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=venue.venue_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		# HttpResponseRedirect("Wedding/")

	return render (request,'venue_details.html',{'VMData':vm_data})


def venuepageANNI(request):
	vm_data= VenueManagement.objects.all()
	if request.method=="POST":
		venue_id = request.POST["venue_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='venue')
		venue=VenueManagement.objects.get(pk=venue_id)
		reguest_for= venue.venue_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=venue.venue_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		# HttpResponseRedirect("Anniversary/")

	return render (request,'venue_details_anni.html',{'VMData':vm_data})

def venuebpage(request):
	vbb_data= VenuebbManagement.objects.all()
	if request.method=="POST":
		venueb_id = request.POST["venueb_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='venue')
		venueb=VenuebbManagement.objects.get(pk=venueb_id)
		request_for= venueb.venueb_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=venueb.venueb_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= request_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		# HttpResponseRedirect("Birthday/")

	return render (request,'venuebb_details.html',{'VBBData':vbb_data})

def cateringpage(request):
	cs_data= CateringService.objects.all()
	if request.method=="POST":
		cat_id = request.POST["cat_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='catering service')
		cat=CateringService.objects.get(pk=cat_id)
		reguest_for= cat.cat_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=cat.cat_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		# HttpResponseRedirect("Wedding/")

	return render (request,'catering_details.html',{'CSData':cs_data})


def cateringpageBIRTHDAY(request):
	cs_data= CateringService.objects.all()
	if request.method=="POST":
		cat_id = request.POST["cat_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='catering service')
		cat=CateringService.objects.get(pk=cat_id)
		reguest_for= cat.cat_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=cat.cat_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		# HttpResponseRedirect("Birthday/")

	return render (request,'catering_details_birthday.html',{'CSData':cs_data})

def cateringpageANNI(request):
	cs_data= CateringService.objects.all()
	if request.method=="POST":
		cat_id = request.POST["cat_id"]
		request_id= f'REQ#{random.randint(00000,99999999)}'
		booking_type= ServiceFor.objects.get(servicefor__icontains='catering service')
		cat=CateringService.objects.get(pk=cat_id)
		reguest_for= cat.cat_name
		request_user= request.user
		requestor_name= request.POST["requestor_name"]
		request_user_phone= request.POST["request_user_phone"]
		request_booking_date =request.POST["bookingdate"]
		location=cat.cat_location
		booking_status=BookingStatus.objects.get(pk=1)


		booking_request= BookingManagement(
		request_id= request_id,
		booking_type= booking_type,reguest_for= reguest_for,
		request_user= request_user,
		requestor_name= requestor_name,
		request_user_phone= request_user_phone,
		request_booking_date =request_booking_date,
		location=location)
		booking_request.save()
		# HttpResponseRedirect("Anniversary/")

	return render (request,'catering_details_anni.html',{'CSData':cs_data})

def user_request_status(request):
	booking= BookingManagement.objects.filter(request_user=request.user).exclude(booking_status=5)
	approved_booking= BookingManagement.objects.filter(request_user=request.user ,booking_status= BookingStatus.objects.get(pk=5))
	print(approved_booking)
	return render(request,'view_request_status.html',{'bookings':booking,'approved_bookings':approved_booking})

def admindashboard(request):
	pending_request= BookingManagement.objects.filter(booking_status=BookingStatus.objects.get(status__icontains='Pending'))
	request_history= BookingManagement.objects.all().exclude(booking_status=BookingStatus.objects.get(status__icontains='Pending with Admin')).exclude(booking_status=BookingStatus.objects.get(status__icontains='Auto Rejected'))
	booking_status=BookingStatus.objects.exclude(pk=4).exclude(pk=2).exclude(pk=1)
	for preq in request_history:
		if preq.booking_status==BookingStatus.objects.get(pk=1):
			bookreq = BookingManagement.objects.get(pk=preq.id)
			bookreq.booking_status=BookingStatus.objects.get(pk=2)
			bookreq.save()
	if request.method=="POST":
		status_change= request.POST['status_change']
		booking_id=request.POST['bookid']
		msg = request.POST['remarks']
		if len(status_change)<=1:
			status = BookingManagement.objects.get(pk=booking_id)
			status.booking_status= BookingStatus.objects.get(pk=status_change)
			status.status_change_message =msg
			# status.last_chage_history=date.today()
			status.save()
			messages.success(request, 'Status has been changed')
			return render (request,'admin_dashboard.html',{'pending_requests':pending_request,'bookings_status':booking_status,'request_histories':request_history})


		else:
			messages.warning(request, 'No Action has been taken !')


	return render (request,'admin_dashboard.html',{'pending_requests':pending_request,'bookings_status':booking_status,'request_histories':request_history})


def new_makup(request):
	mkfm= FormNewMakeupArtist()
	if request.method=="POST":
		mkfm = FormNewMakeupArtist(request.POST, request.FILES)
		if mkfm.is_valid():
			mkfm.save()
			messages.success(request, 'MakeupArtist Information Added Successfully!')
			return HttpResponseRedirect("/admindashboard/")

	return render (request,'new_makeup_artist.html',{"makeup_form":mkfm})

def bpackage(request):
		pkg_b=PackageManagement.objects.all().filter(event_type='Birthday')
		pkg_a=PackageManagement.objects.all().filter(event_type='Anniversary')
		pkg_w=PackageManagement.objects.filter(event_type__startswith="Mar")#all().filter(event_type='Marriage')
		if request.method=="POST":
			package_id = request.POST["package_id"]
			request_id= f'REQ#{random.randint(00000,99999999)}'
			booking_type= ServiceFor.objects.get(servicefor__icontains='package')
			pkg=PackageManagement.objects.get(pk=package_id)
			reguest_for= pkg.event_type
			request_user= request.user
			requestor_name= request.POST["requestor_name"]
			request_user_phone= request.POST["request_user_phone"]
			request_booking_date =request.POST["bookingdate"]
			booking_status=BookingStatus.objects.get(pk=1)

			booking_request= BookingManagement(
			request_id= request_id,
			booking_type= booking_type,reguest_for= reguest_for,
			request_user= request_user,
			requestor_name= requestor_name,
			request_user_phone= request_user_phone,
			request_booking_date =request_booking_date,
			)
			booking_request.save()
		return render (request,'Packages.html',{'Pack_b':pkg_b,'Pack_a':pkg_a,'Pack_w':pkg_w,})
def wpackage(request):
    pkg=PackageManagement.objects.all().filter(event_type='Marriage')[:3]
    return render (request,'wedding package.html',{'Pack':pkg})
