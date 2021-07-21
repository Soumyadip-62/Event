from django.db import models
#BRIDE
#makeup related models
specification_choices=[
    ('',''),
    ('MAC', 'MAC'),
    ('Normal', 'Normal'),
]



class ServiceFor(models.Model):
    servicefor= models.CharField(max_length=30)
    servicefor_desc= models.CharField(max_length=300,blank=True)
    servicefor_log= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.servicefor


class Location(models.Model):
    location= models.CharField(max_length=30)
    location_desc= models.CharField(max_length=300,blank=True)
    location_log= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.location

#ANNIVERSARY_special
name_choices=[
    ('Anniversary Special Decor','decor'),
    ('Anniversary Special Dinner','dinner'),
    ('Anniversary Special Floatel Party','Floatel party'),
]
class AnniSpecial(models.Model):
    arrengement_name = models.CharField(max_length=100,blank=True,choices=name_choices,)
    organizer= models.CharField(max_length=100)
    phone= models.CharField(max_length=30)
    location= models.CharField(max_length=30)
    package=  models.CharField(max_length=30)
    desc= models.CharField(max_length=500,blank=True)
    log= models.DateTimeField(auto_now_add=True)
    picture= models.ImageField(upload_to="Anni",blank=True)
    servicefor=  models.ForeignKey(ServiceFor,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.arrengement_name

class AnniTheme(models.Model):
    theme_name = models.CharField(max_length=100,blank=True,)
    package=  models.CharField(max_length=30)
    desc= models.CharField(max_length=500,blank=True)
    log= models.DateTimeField(auto_now_add=True)
    picture= models.ImageField(upload_to="Anni",blank=True)
    back_pic= models.ImageField(upload_to="Anni",blank=True)
    servicefor=  models.ForeignKey(ServiceFor,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.theme_name

yr_choices=[
    ('1st Anniversary Celebration','1'),
    ('2nd Anniversary Celebration','2'),
    ('3rd Anniversary Celebration','3'),
    ('4th Anniversary Celebration','4'),
    ('5th Anniversary Celebration','5'),
    ('6th Anniversary Celebration','6'),
    ('7th Anniversary Celebration','7'),
    ('8th Anniversary Celebration','8'),
    ('9th Anniversary Celebration','9'),
    ('10th Anniversary Celebration','10'),
    ('11th Anniversary Celebration','11'),
    ('12th Anniversary Celebration','12'),
    ('13th Anniversary Celebration','13'),
    ('14th Anniversary Celebration','14'),
    ('15th Anniversary Celebration','15'),
    ('16th Anniversary Celebration','16'),
    ('17th Anniversary Celebration','17'),
    ('18th Anniversary Celebration','18'),
    ('19th Anniversary Celebration','19'),
    ('20th Anniversary Celebration','20'),
    ('Silver Anniversary Celebration','25'),
    ('Golden Anniversary Celebration','50'),
]

class AnniPics(models.Model):
    type = models.CharField(max_length=100,blank=True,choices=yr_choices,)
    desc= models.CharField(max_length=500,blank=True)
    picture= models.ImageField(upload_to="Anni",blank=True)
    def __str__(self):
        return self.type

#Birthday
class BirthdayPics(models.Model):
    type = models.CharField(max_length=100,blank=True)
    desc= models.CharField(max_length=500,blank=True)
    picture= models.ImageField(upload_to="Birthday",blank=True)
    def __str__(self):
        return self.type

#Wedding
class WeddPics(models.Model):
    type = models.CharField(max_length=100,blank=True,)
    desc= models.CharField(max_length=500,blank=True)
    picture= models.ImageField(upload_to="Wedding",blank=True)
    def __str__(self):
        return self.type

class MakeupType(models.Model):
    type = models.CharField(max_length=30)
    type_desc= models.CharField(max_length=300,blank=True)
    mtype_log= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class MakeupArtist(models.Model):
    mua_name = models.CharField(max_length=50)
    type= models.ForeignKey(MakeupType,on_delete=models.CASCADE)
    mua_phone= models.CharField(max_length=30)
    mua_location= models.ForeignKey(Location,on_delete=models.CASCADE)
    mua_office = models.CharField(max_length=30,blank=True)
    package=  models.CharField(max_length=30)
    specification=  models.CharField(max_length=30,blank=True,choices=specification_choices,)
    mu_desc= models.CharField(max_length=300,blank=True)
    mua_log= models.DateTimeField(auto_now_add=True)
    picture= models.ImageField(upload_to="MUAs",blank=True)
    servicefor=  models.ForeignKey(ServiceFor,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.mua_name

#mehedi related models


#CATERING SERVICES
catering_choices=[
    ('',''),
    ('Veg', 'Veg'),
    ('Non-Veg', 'Non Veg'),
    ('Pure Veg', 'Pure Veg'),
]


class CateringService(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_type= models.CharField(max_length=30,blank=True,choices=catering_choices,)
    cat_phone= models.CharField(max_length=30)
    cat_location= models.ForeignKey(Location,on_delete=models.CASCADE)
    cat_office = models.CharField(max_length=30,blank=True)
    rate=  models.CharField(max_length=30)
    cat_desc= models.CharField(max_length=300,blank=True)
    cat_log= models.DateTimeField(auto_now_add=True)
    cat_picture= models.ImageField(upload_to="Catering",blank=True)
    servicefor= models.ForeignKey(ServiceFor,on_delete=models.CASCADE,default=2)
    def __str__(self):
        return self.cat_name

#venue
venue_choices=[
    ('',''),
    ('Marriage Hall', 'Marriage Hall'),
    ('Conference Hall', 'Conference Hall'),
    ('Auditorium', 'Auditorium'),
    ('Party Hall', 'Party Hall'),
    ('Party Ground', 'Party Ground'),
    ('Birthday Hall','Birthday Hall'),
]

class VenueType(models.Model):
    type = models.CharField(max_length=30)
    type_desc= models.CharField(max_length=300,blank=True)
    vtype_log= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class VenueManagement(models.Model):
    venue_name = models.CharField(max_length=50)
    venue_type= models.CharField(max_length=30,blank=True,choices=venue_choices,)
    venue_phone= models.CharField(max_length=30)
    venue_location= models.ForeignKey(Location,on_delete=models.CASCADE)
    venue_office = models.CharField(max_length=30,blank=True)
    venue_rate=  models.CharField(max_length=30)
    venue_desc= models.CharField(max_length=300,blank=True)
    venue_log= models.DateTimeField(auto_now_add=True)
    venue_picture= models.ImageField(upload_to="venues",blank=True)
    servicefor=  models.ForeignKey(ServiceFor,on_delete=models.CASCADE,default=3)
    def __str__(self):
        return self.venue_name


venuebb_choices=[
    ('',''),
    ('Party Hall', 'Party Hall'),
    ('Birthday Kid Hall','Birthday Kid Hall'),
]

class VenuebType(models.Model):
    type = models.CharField(max_length=30)
    type_desc= models.CharField(max_length=300,blank=True)
    vtype_log= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class VenuebbManagement(models.Model):
    venueb_name = models.CharField(max_length=50)
    venueb_type= models.CharField(max_length=30,blank=True,choices=venuebb_choices,)
    venueb_phone= models.CharField(max_length=30)
    venueb_location= models.ForeignKey(Location,on_delete=models.CASCADE)
    venueb_office = models.CharField(max_length=30,blank=True)
    venueb_rate=  models.CharField(max_length=30)
    venueb_desc= models.CharField(max_length=300,blank=True)
    venueb_log= models.DateTimeField(auto_now_add=True)
    venueb_picture= models.ImageField(upload_to="venuebs",blank=True)
    servicefor=  models.ForeignKey(ServiceFor,on_delete=models.CASCADE,default=3)
    def __str__(self):
        return self.venueb_name

class BookingStatus(models.Model):
    status = models.CharField(max_length=50)
    status_desc= models.CharField(max_length=300,blank=True)
    status_log= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status

class BookingManagement(models.Model):
    request_id=models.CharField(max_length=100)
    booking_type=  models.ForeignKey(ServiceFor,on_delete=models.CASCADE)
    reguest_for= models.CharField(max_length=50)
    request_user= models.CharField(max_length=50)
    requestor_name=models.CharField(max_length=50)
    request_user_phone= models.CharField(max_length=10)
    request_booking_date =models.DateField()
    location=models.CharField(max_length=50)
    booking_status= models.ForeignKey(BookingStatus,on_delete=models.CASCADE,default=1)
    status_change_message= models.CharField(max_length=500,blank=True) #remakes
    last_chage_history= models.DateField(auto_now_add=True,blank=True)
    booking_request_log= models.DateField(auto_now_add=True,blank=True)
    
Decor_choices=[
    ('',''),
    ('Marriage', 'Marriage'),
    ('Birthday', 'Birthday'),
    ('Anniversary', 'Anniversary'),
    
]



    
class PhotoGrapher(models.Model):
    pht_name = models.CharField(max_length=30,primary_key=True)
    pht_adress = models.CharField(max_length=30,)  
    pht_profile = models.CharField(max_length=80,)
    pht_range = models.CharField(max_length=30,)
    pht_sample1 = models.ImageField(upload_to="Photographer",blank=True)
    pht_sample2 = models.ImageField(upload_to="Photographer",blank=True)
    pht_sample3 = models.ImageField(upload_to="Photographer",blank=True)
    def __str__(self):
        return self.pht_name

class Decorator(models.Model):
    dec_name = models.CharField(max_length=30,primary_key=True)  
    dec_style = models.CharField(max_length=30,choices=Decor_choices)
    dec_location = models.CharField(max_length=50,)
    dec_range = models.CharField(max_length=30,)
    dec_thumbnail = models.ImageField(upload_to="decor",blank=True)
    def __str__(self):
        return self.dec_name
    
Event_choices=[
    ('',''),
    ('Marriage', 'Marriage'),
    ('Birthday', 'Birthday'),
    ('Anniversary', 'Anniversary'),
    
]

class PackageManagement(models.Model):
    #package_id= models.CharField(max_length=10,blank=True)
    event_type= models.CharField(max_length=30,choices=Event_choices)
    event_venue= models.ForeignKey(VenueManagement,on_delete=models.CASCADE,blank=True)
    event_caterer= models.ForeignKey(CateringService,on_delete=models.CASCADE,blank=True)
    event_mua= models.ForeignKey(MakeupArtist,on_delete=models.CASCADE,blank=True)
    event_thumbnail= models.ImageField(upload_to="package",blank=True)
    event_decor= models.ForeignKey(Decorator,on_delete=models.CASCADE,blank=True)
    event_rate=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.event_type

#Create your Contact Modal.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    feedbacks=models.TextField()
    def __str__(self):
        return self.name
