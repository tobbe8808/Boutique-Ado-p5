from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def custom_page_not_found_view(request, exception):
    return render(request, "home/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "home/500.html", {})
