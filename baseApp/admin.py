from django.contrib import admin
from .models import MakeupArtist,MakeupType,CateringService,VenueManagement,VenuebbManagement,Location,ServiceFor,BookingManagement,BookingStatus,Location,ServiceFor,BookingManagement,BookingStatus,AnniSpecial,AnniTheme,AnniPics,BirthdayPics,WeddPics,PhotoGrapher,Decorator,PackageManagement,Contact


@admin.register(MakeupArtist)
class AdminMakeupArtist(admin.ModelAdmin):
    list_display=['mua_name','type','mua_phone','package','specification','picture']

@admin.register(AnniSpecial)
class AdminAnniSpecial(admin.ModelAdmin):
    list_display=['arrengement_name','organizer','phone','location','package','desc','log','picture','servicefor']

@admin.register(AnniTheme)
class AdminAnniTheme(admin.ModelAdmin):
    list_display=['id','theme_name','package','desc','log','picture','back_pic','servicefor']

@admin.register(AnniPics)
class AdminAnniPics(admin.ModelAdmin):
    list_display=['id','type','desc','picture',]

@admin.register(BirthdayPics)
class AdminBirthdayPics(admin.ModelAdmin):
    list_display=['id','type','desc','picture',]


@admin.register(WeddPics)
class AdminWeddPics(admin.ModelAdmin):
    list_display=['id','type','desc','picture',]

@admin.register(MakeupType)
class AdminMakeupType(admin.ModelAdmin):
    list_display=['id','type','type_desc','mtype_log']

@admin.register(CateringService)
class AdminCateringService(admin.ModelAdmin):
    list_display=['id','cat_name','cat_type','cat_phone','rate']

@admin.register(VenueManagement)
class AdminVenueManagement(admin.ModelAdmin):
    list_display=['id','venue_name','venue_type','venue_phone','venue_location','venue_rate','venue_picture']

@admin.register(VenuebbManagement)
class AdminVenuebbManagement(admin.ModelAdmin):
    list_display=['id','venueb_name','venueb_type','venueb_phone','venueb_location','venueb_rate','venueb_picture']

@admin.register(Location)
class AdminLocation(admin.ModelAdmin):
    list_display=['id','location','location_desc']


@admin.register(ServiceFor)
class AdminServiceFor(admin.ModelAdmin):
    list_display=['id','servicefor']


@admin.register(BookingManagement)
class AdminBookingManagement(admin.ModelAdmin):
    list_display=['booking_type','reguest_for','requestor_name','request_user','request_user_phone','request_booking_date','location','booking_status']


#
@admin.register(BookingStatus)
class AdminBookingStatus(admin.ModelAdmin):
    list_display=['id','status']

#
# @admin.register(ServiceFor)
# class AdminServiceFor(admin.ModelAdmin):
#     list_display=['id','servicefor']

#
# @admin.register(ServiceFor)
# class AdminServiceFor(admin.ModelAdmin):
#     list_display=['id','servicefor']

#
# @admin.register(ServiceFor)
# class AdminServiceFor(admin.ModelAdmin):
#     list_display=['id','servicefor']
@admin.register(Decorator)
class AdminDecorator(admin.ModelAdmin):
    list_display=['dec_name','dec_style','dec_location','dec_range','dec_thumbnail']
@admin.register(PhotoGrapher)
class AdminPhotoGrapher(admin.ModelAdmin):
    list_display=['pht_name','pht_adress','pht_profile','pht_range','pht_sample1','pht_sample2','pht_sample3']
@admin.register(PackageManagement)
class AdminPackageManagement(admin.ModelAdmin):
    list_display=['id','event_type','event_venue','event_caterer','event_mua','event_thumbnail','event_decor'] 
   
# Admin of contact
admin.site.register(Contact)   