
from django.contrib import admin
from .models import Availability

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('provider', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('provider', 'day_of_week')
    ordering = ('provider', 'day_of_week', 'start_time')
    search_fields = ('provider__username',)

    def get_queryset(self, request):
        """Limit the view to only providers if needed."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(provider=request.user)


