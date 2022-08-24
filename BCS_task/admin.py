from django.contrib import admin

from .models import *


class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_id', 'description', 'time_create')
    list_display_links = ('transaction_id', )
    search_fields = ('transaction_id', )


admin.site.register(Translation, TranslationAdmin)
