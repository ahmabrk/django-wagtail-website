from django.shortcuts import render
from wagtail.models import Page


def search(request):
    query = request.GET.get('q', '').strip()
    results = Page.objects.live().search(query) if query else Page.objects.none()
    template = 'search/partials/results.html' if request.headers.get('HX-Request') else 'search/search.html'
    return render(request, template, {'query': query, 'results': results})
