from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    class Meta:
        model = User
        fields = '__all__'


