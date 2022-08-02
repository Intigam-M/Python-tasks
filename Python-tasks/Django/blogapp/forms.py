from django.forms import ModelForm
from blogapp.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'