from django import forms

from .models import Courier, Locker, Parcel


class ParcelCreateForm(forms.Form):
    sender_name = forms.CharField(label="Nadawca", max_length=120)
    recipient_name = forms.CharField(label="Odbiorca", max_length=120)
    recipient_phone = forms.CharField(label="Telefon odbiorcy", max_length=20)
    locker = forms.ModelChoiceField(label="Paczkomat", queryset=Locker.objects.all())
    courier = forms.ModelChoiceField(label="Kurier", queryset=Courier.objects.all(), required=False)

    def clean_locker(self):
        locker = self.cleaned_data["locker"]
        if not locker.has_free_slot():
            raise forms.ValidationError("Ten paczkomat jest pelny. Wybierz inny punkt.")
        return locker
