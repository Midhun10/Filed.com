from .models import Song,AudioType,AudioBook,Podcast
from django.forms import ModelForm
from django import forms
from datetime import datetime

class DateInput(forms.DateInput):
        input_type = 'date'

class TimeInput(forms.TimeInput):
        input_type = 'time'

class AudioTypeForm(ModelForm):
    class Meta:
        model = AudioType
        fields = "__all__"

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
        widgets = {
            'Song_Name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Song Name'}),
            'Song_Duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'Song_Uploadtime' : TimeInput(attrs={'class': 'form-control'}),
            'Song_Uploaddate' : DateInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super(SongForm, self).clean()
        # here all fields have been validated individually,
        # and so cleaned_data is fully populated
        my_date = cleaned_data.get('Song_Uploaddate')
        my_time = cleaned_data.get('Song_Uploadtime')
        print(datetime.now())
        if my_date and my_time:
            my_date_time = datetime.combine(my_date,my_time)
            my_date_time = datetime.strptime(str(my_date_time), '%Y-%m-%d %H:%M:%S')
            if datetime.now() > my_date_time:
                self._errors['Song_Uploaddate'] = self.error_class(['Wrong Uploaddate'])
                self._errors['Song_Uploadtime'] = self.error_class(['Wrong Uploadtime'])
        return cleaned_data

class AudioBookForm(ModelForm):
    class Meta:
        model = AudioBook
        fields = "__all__"
        widgets = {
            'Book_Title' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Book Name'}),
            'Book_Author' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Book Author'}),
            'Book_Narrator' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Book Narrator'}),
            'Book_Duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'Book_Uploadtime' : TimeInput(attrs={'class': 'form-control'}),
            'Book_Uploaddate' : DateInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super(AudioBookForm, self).clean()
        # here all fields have been validated individually,
        # and so cleaned_data is fully populated
        my_date = cleaned_data.get('Book_Uploaddate')
        my_time = cleaned_data.get('Book_Uploadtime')
        print(datetime.now())
        if my_date and my_time:
            my_date_time = datetime.combine(my_date,my_time)
            my_date_time = datetime.strptime(str(my_date_time), '%Y-%m-%d %H:%M:%S')
            if datetime.now() > my_date_time:
                self._errors['Book_Uploaddate'] = self.error_class(['Wrong Uploaddate'])
                self._errors['Book_Uploadtime'] = self.error_class(['Wrong Uploadtime'])
        return cleaned_data

class PodcastForm(ModelForm):
    class Meta:
        model = Podcast
        fields = "__all__"
        widgets = {
            'Podcast_Name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Podcast Name'}),
            'Podcast_Host' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Podcast Host'}),
            'Podcast_Participants_Count' : forms.NumberInput(attrs={'class': 'form-control'}),
            'Podcast_Duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'Podcast_Uploadtime' : TimeInput(attrs={'class': 'form-control'}),
            'Podcast_Uploaddate' : DateInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super(PodcastForm, self).clean()
        # here all fields have been validated individually,
        # and so cleaned_data is fully populated
        my_date = cleaned_data.get('Podcast_Uploaddate')
        my_time = cleaned_data.get('Podcast_Uploadtime')
        print(datetime.now())
        if my_date and my_time:
            my_date_time = datetime.combine(my_date,my_time)
            my_date_time = datetime.strptime(str(my_date_time), '%Y-%m-%d %H:%M:%S')
            if datetime.now() > my_date_time:
                self._errors['Podcast_Uploaddate'] = self.error_class(['Wrong Uploaddate'])
                self._errors['Podcast_Uploadtime'] = self.error_class(['Wrong Uploadtime'])
        return cleaned_data