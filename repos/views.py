from django.shortcuts import render, redirect, get_object_or_404
from .models import Repository, File, Version
from .forms import RepositoryForm, FileForm, VersionForm
from .utils import compare_files

def repository_list(request):
    repositories = Repository.objects.all()
    return render(request, 'repository/repository_list.html', {'repositories': repositories})

def repository_detail(request, pk):
    repository = get_object_or_404(Repository, pk=pk)
    return render(request, 'repository/repository_detail.html', {'repository': repository})

def create_repository(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repository_list')
    else:
        form = RepositoryForm()
    return render(request, 'repository/repository_form.html', {'form': form})

def create_file(request, repository_pk):
    repository = get_object_or_404(Repository, pk=repository_pk)
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            file = form.save(commit=False)
            file.repository = repository
            file.save()
            return redirect('repository_detail', pk=repository_pk)
    else:
        form = FileForm()
    return render(request, 'repository/file_form.html', {'form': form})

def create_version(request, file_pk):
    file = get_object_or_404(File, pk=file_pk)
    if request.method == 'POST':
        form = VersionForm(request.POST, request.FILES)
        if form.is_valid():
            version = form.save(commit=False)
            version.file = file
            version.version_number = file.version_set.count() + 1
            version.save()
            return redirect('repository_detail', pk=file.repository.pk)
    else:
        form = VersionForm()
    return render(request, 'repository/version_form.html', {'form': form})

def compare_versions(request, file_pk, version1_pk, version2_pk):
    file = get_object_or_404(File, pk=file_pk)
    version1 = get_object_or_404(Version, pk=version1_pk, file=file)
    version2 = get_object_or_404(Version, pk=version2_pk, file=file)
    
    with version1.uploaded_file.open() as v1:
        version1_content = v1.read().decode('utf-8')
    with version2.uploaded_file.open() as v2:
        version2_content = v2.read().decode('utf-8')
    
    comparison_result = compare_files(version1_content, version2_content)
    return render(request, 'repository/comparison_result.html', {
        'file': file,
        'version1': version1,
        'version2': version2,
        'comparison_result': comparison_result
    })
