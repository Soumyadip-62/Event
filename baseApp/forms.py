from django import forms
from .models import BookingManagement,MakeupArtist
from django.core.validators import MaxLengthValidator



class FormBookingStatus(forms.ModelForm):

    class Meta:
        model= BookingManagement
        labels={"booking_status" : "Status",'status_change_message':'Remarks'}

        fields=['booking_status','status_change_message']
        widgets = {

            'booking_status': forms.Select(attrs={'class':'form-control'}),
            'status_change_message': forms.TextInput(attrs={'class':'form-control'}),

        }

class FormNewMakeupArtist(forms.ModelForm):

    class Meta:
        model= MakeupArtist
        labels={"mua_name" : "Artist Name",
                'type':'Type of Makeup',
                'mua_phone':'Phone Number',
                'mua_location':'Location',
                'mua_office':'Office',
                'package':'Package/Person',
                'mu_desc':'Package Description',
                'picture': "Display Picture"
        }

        fields=['mua_name','type','mua_phone','mua_location','mua_office','package','specification','mu_desc','picture']
        #validators=["mua_name":[MaxLengthValidator(200)]]
        
        widgets = {

            'picture': forms.FileInput(attrs={'class':'form-control'}),
            'mua_name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'mua_phone': forms.TextInput(attrs={'class':'form-control'}),
            'mua_location':forms.Select(attrs={'class':'form-control'}),
            'mua_office':forms.TextInput(attrs={'class':'form-control'}),
            'package':forms.TextInput(attrs={'class':'form-control'}),
            'mu_desc':forms.Textarea(attrs={'class':'form-control'}),
            'specification':forms.Select(attrs={'class':'form-control'}),
        }
