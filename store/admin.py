from django.contrib import admin
from .models import Product, Variation
from django import forms
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from django.utils.html import format_html

# Register your models here.
# Formulaire personnalisé pour les champs de VariationInline
class VariationInlineForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = '__all__'
        widgets = {
            'variation_category': forms.Select(attrs={'class': 'custom-select', 'style': 'width: 200px; color: black;'}),
            'variation_value': forms.TextInput(attrs={'class': 'custom-input', 'style': 'width: 250px; font-weight: bold;  color: black;'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'custom-checkbox', 'style': 'transform: scale(1.5);'}),
        }

# Inline admin pour afficher les variations dans ProductAdmin
class VariationInline(admin.TabularInline):  
    model = Variation
    form = VariationInlineForm 
    extra = 2  # Nombre de lignes vides par défaut
    fields = ('variation_category', 'variation_value', 'is_active')
    fk_name = 'product'  # Spécifie la clé étrangère vers Product
    classes = ['collapse']  # Ajoute une option de repli pour améliorer l'affichage


class ProductAdmin(UnfoldModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('image_tag', 'product_name', 'price', 'stock', 'category', 'modified_date', 'created_date', 'is_available')
    list_display_links = ('product_name',)
    list_filter = ('category', 'created_date', 'is_available')
    list_editable = ('is_available',)
    search_fields = ('product_name', 'category__category_name')
    list_per_page = 20
    inlines = [VariationInline]

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.image.url)
        return "Pas d'image"

    image_tag.short_description = 'Image'  # Nom de la colonne

class VariationAdmin(UnfoldModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_filter = ('product', 'variation_category', 'variation_value')
    list_editable = ('is_active',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

