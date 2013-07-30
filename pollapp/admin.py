from django.contrib import admin
from pollapp.models import Poll,Choice



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
#    date_hierarchy = 'pub_date'
    list_display = ('question', 'pub_date','was_published_recently')

admin.site.register(Poll, PollAdmin)

