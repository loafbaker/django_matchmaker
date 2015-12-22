from django import forms

from .models import Profile, UserJob

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'location',
            'picture',
        ]


class UserJobForm(forms.ModelForm):
    class Meta:
        model = UserJob
        fields = [
            'position',
            'location',
            'employer_name',
        ]

