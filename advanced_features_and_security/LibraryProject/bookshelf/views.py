from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Document

@permission_required('app_name.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        # Add logic for updating the document
        pass
    return render(request, 'edit_document.html', {'document': document})

@permission_required('app_name.can_create', raise_exception=True)
def create_document(request):
    if request.method == "POST":
        # Add logic for creating a new document
        pass
    return render(request, 'create_document.html')
@permission_required('app_name.can_delete', raise_exception=True)
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        document.delete()
        return redirect('document_list')
    return render(request, 'delete_document.html', {'document': document})
