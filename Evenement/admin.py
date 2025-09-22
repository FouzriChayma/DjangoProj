from django.contrib import admin
from .models import Evenement, Participation_event
from datetime import date  
from django.contrib import messages


class Evet_Filter(admin.SimpleListFilter):
    title = 'Event Date Filter'
    parameter_name = 'evt_date'
    
    def lookups(self, request, model_admin):
        return (
            ('PE', 'Past Events'),
            ('UE', 'Upcoming Events'),
            ('TE', 'Today Events'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'PE':
            return queryset.filter(evt_date__lt=date.today()) 
        elif self.value() == 'UE':
            return queryset.filter(evt_date__gt=date.today())  
        elif self.value() == 'TE':
            return queryset.filter(evt_date=date.today())     
        return queryset

class Participations(admin.TabularInline):
    model = Participation_event  
    extra = 1
    readonly_fields = ('participation_date',)


@admin.register(Evenement) # fi 3oudh admin.site.register(Evenement, EvenementAdmin)
class EvenementAdmin(admin.ModelAdmin):
    actions = ['accept_status']  

    def accept_status(self, request, queryset):
        rowupdate = queryset.update(statut=True)
        if rowupdate == 1:
            msg = "1 event was"
        else:
            msg = f"{rowupdate} events were"
        messages.success(request, f"{msg} successfully marked as accepted.")
    accept_status.short_description = "Mark selected events as accepted"

    list_display = ('title', 'statut', 'evt_date', 'category', 'Organizer')
    list_filter = ['category', 'statut', Evet_Filter]
    search_fields = ('title', 'description')
    date_hierarchy = 'evt_date'
    list_per_page = 1

    inlines = [Participations] 
    readonly_fields = ('created_at', 'updated_at')
    #fieldsets = (
    #    ('Dates', {'fields': ('created_at', 'updated_at')}),
    #)
    autocomplete_fields = ['Organizer']  # <-- this enables autocomplete
#admin.site.register(Evenement, EvenementAdmin)
@admin.register(Participation_event)
class ParticipationEventAdmin(admin.ModelAdmin): 
    pass