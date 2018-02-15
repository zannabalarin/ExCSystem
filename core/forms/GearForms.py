from django import forms
from core.models import Gear


class GearCreationForm(forms.ModelForm):
    """
    The basic form to create a piece of Gear. Mostly follows django admin defaults

    This uses the ModelForm (like the rest of django's admin) to automatically translate the model into a Form, View and
    the related HTML. Therefore, what is contained here simply overrides some default functionality, and explicit views
    and templates may not be present.
    """

    class Meta:
        model = Gear


class GearRetagForm(forms.ModelForm):
    """
    Form to expedite the process of re-taging (changing the RFID) a piece of gear

    This uses the ModelForm (like the rest of django's admin) to automatically translate the model into a Form, View and
    the related HTML. Therefore, what is contained here simply overrides some default functionality, and explicit views
    and templates may not be present.
    """

    class Meta:
        model = Gear