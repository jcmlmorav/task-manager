from django.forms import ModelForm
from .models import Project, Stage

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description'
        ]

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = [
            'name'
        ]
