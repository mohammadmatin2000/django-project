from django.forms import ModelForm
from app.models import Contact
from captcha.fields import CaptchaField
# ======================================================================================================================
class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
# ======================================================================================================================