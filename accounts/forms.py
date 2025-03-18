from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'username',)
        help_text = {
            'email': 'none',
            'username': 'none',
            
        }
        
        
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'username',)
        