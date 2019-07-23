from django.contrib import admin
from .models import Card, CardPostTag, CardChemicalTag, CardComment, CardReComment
from django_summernote.admin import SummernoteModelAdmin


class CardModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'



admin.site.register(Card, CardModelAdmin)
admin.site.register(CardPostTag)
admin.site.register(CardChemicalTag)
admin.site.register(CardComment)
admin.site.register(CardReComment)