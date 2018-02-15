from django import forms
from core.models import Gear


class GearBeginCreateForm(forms.ModelForm):
    """
    The basic form to create a piece of Gear. Mostly follows django admin defaults

    This creates a generic piece of gear and based on that information redirects to a more specific gear creation form

    This uses the ModelForm (like the rest of django's admin) to automatically translate the model into a Form, View and
    the related HTML. Therefore, what is contained here simply overrides some default functionality, and explicit views
    and templates may not be present.
    """

    class Meta:
        model = Gear
        fields = ("department", "rfid")


class GearFinishForm(forms.ModelForm):
    """
    Form to complete filling out data the data required for a specific type of gear

    This form is redirected to based on the choices made in the GearBeginCreateForm. It should adjust the data it
    requires based on the exact type of gear that was chosen
    """

    pass


class GearReTagForm(forms.ModelForm):
    """
    Form to expedite the process of re-taging (changing the RFID) a piece of gear

    This uses the ModelForm (like the rest of django's admin) to automatically translate the model into a Form, View and
    the related HTML. Therefore, what is contained here simply overrides some default functionality, and explicit views
    and templates may not be present.
    """

    class Meta:
        model = Gear
        fields = ("rfid", )