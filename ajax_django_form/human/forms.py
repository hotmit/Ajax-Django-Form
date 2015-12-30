from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit
from django import forms
from django.core.exceptions import ValidationError
from ajax_django_form.human.models import PunyHuman
from django.utils.translation import ugettext as _


class PunyHumanForm(forms.ModelForm):

    class Meta:
        model = PunyHuman
        excludes = []

    def clean_level_of_hotness(self):
        level = self.cleaned_data['level_of_hotness']
        if level < 2:
            raise ValidationError(_('Don\'t be so mean!'))
        return level

    def __init__(self, *args, **kwargs):
        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'create/'
        helper.form_class = 'dj-ajax-form'
        helper.add_input(Button('reset', _('Reset'), css_class='btn btn-warning'))
        helper.add_input(Submit('create', _('Create')))

        self.helper = helper
        super().__init__(*args, **kwargs)


class PunyHumanUpdateForm(PunyHumanForm):
    id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'update/'
        helper.form_class = 'dj-ajax-form'
        helper.add_input(Button('reset', _('Reset'), css_class='btn btn-warning'))
        helper.add_input(Submit('update', _('Update')))
        self.helper = helper