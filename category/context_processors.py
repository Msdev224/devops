from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)  # This will make the links available to all templates