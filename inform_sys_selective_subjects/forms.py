from django import forms

from inform_sys_selective_subjects.models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('part', 'code', 'name', 'majoring', 'department', 'level',
                  'semester', 'language', 'preconditions', 'what_is_being_studied',
                  'why_should_be_studied', 'what_can_be_learned', 'how_to_use',
                  'information_provision', 'educational_activities_type',
                  'semester_control_type', 'max_capacity', 'min_capacity')
