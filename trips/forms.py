from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['trip', 'date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['trip', 'rating', 'comment']