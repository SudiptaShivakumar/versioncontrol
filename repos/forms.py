from django import forms
from .models import Repository, File, Version

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ['name', 'description']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name']

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['uploaded_file']
