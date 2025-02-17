from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from scheduling.models import Availability

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_superuser", "is_premium")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "expertise")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Premium Status", {"fields": ("is_premium", "premium_until")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

admin.site.register(User, CustomUserAdmin)



class AvailabilityInline(admin.TabularInline):  # or admin.StackedInline
    model = Availability
    extra = 1  # Allows adding extra slots easily

class CustomUserAdmin(UserAdmin):
    inlines = [AvailabilityInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
