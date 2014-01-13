from django import forms
from activity.models import Activity
from tools.forms import LtModelForm


class ActivityCreateForm(LtModelForm):
# class ActivityCreateForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ("name","introduction","date","place","price")

    #TODO
    # default creater use login user