from django.contrib import admin
from .models import Ülesanne, AlamÜlesanne

class AlamÜlesanneInline(admin.TabularInline):
    model = AlamÜlesanne
    extra = 1
    fields = ('sisu', 'tehtud')
    show_change_link = True

@admin.register(Ülesanne)
class ÜlesanneAdmin(admin.ModelAdmin):
    list_display = ('pealkiri', 'kasutaja', 'loodud', 'pildi_eelvaade')
    list_filter = ('kasutaja', 'loodud')
    search_fields = ('pealkiri', 'kirjeldus', 'kasutaja__username')
    date_hierarchy = 'loodud'
    inlines = [AlamÜlesanneInline]

    def pildi_eelvaade(self, obj):
        if obj.pilt:
            return f'<img src="{obj.pilt.url}" width="100" style="border-radius: 8px;" />'
        return "-"
    pildi_eelvaade.allow_tags = True
    pildi_eelvaade.short_description = 'Pilt'

@admin.register(AlamÜlesanne)
class AlamÜlesanneAdmin(admin.ModelAdmin):
    list_display = ('sisu', 'ülesanne', 'tehtud')
    list_filter = ('tehtud', 'ülesanne__kasutaja')
    search_fields = ('sisu', 'ülesanne__pealkiri')
