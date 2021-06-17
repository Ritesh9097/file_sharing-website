from user.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ("image","info","gender","mob")
