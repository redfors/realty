from django import forms
from django.contrib import admin
from .models import Realty, StatusesRealty, Images
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields



class RealtyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    description_data = forms.CharField(widget=CKEditorUploadingWidget())
    description_details = forms.CharField(widget=CKEditorUploadingWidget())
    place = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Realty
        fields = '__all__'




class RealtyInline(admin.StackedInline):
    model = Images
    extra = 1


class RealtyAdmin(admin.ModelAdmin):
    list_display = ['name', 'overview', 'get_image']
    readonly_fields = ("get_image",)
    prepopulated_fields = {"url": ("name",)}
    save_as = True
    inlines = [RealtyInline]
    form = RealtyAdminForm
    formfield_overrides = {
        map_fields.AddressField: {'widget':
            map_widgets.GoogleMapsAddressWidget(attrs={
                'data-map-type': 'roadmap'})}}
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src=/static/{obj.image.url} width="50" height="60"')



    get_image.short_description = "Image"
admin.site.register(Realty, RealtyAdmin)


admin.site.register(StatusesRealty)
admin.site.register(Images)