from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import TemporaryUploadedFile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')

    def clean_avatar(self):
        """
        Checks that the size of the uploaded file does not exceed 4MB.
        """
        image: TemporaryUploadedFile = self.cleaned_data.get('avatar', False)
        if image:
            if image.size > 4 * 1024 * 1024:
                raise ValidationError("Размер изображения слишком большой ( > 4mb )")
            return image
