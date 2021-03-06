from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin

from coss.club.models import (ClubRegistration, Club, HomePage, SingleColumn,
                              Interest, Testimonial)

club_extra_fieldsets = (
    (None, {
        "fields": (
            "club_description",
            "city",
            "location",
            "activity",
            "interests",
            "affiliated",
        )
    }),
)


class InterestInline(admin.TabularInline):
    model = Interest.club.through


class ClubAdmin(PageAdmin):
    inlines = (
        InterestInline,
    )
    fieldsets = deepcopy(PageAdmin.fieldsets) + club_extra_fieldsets


class TestimonialAdmin(admin.ModelAdmin):
    pass


class ClubRegistrationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Club, ClubAdmin)
admin.site.register(HomePage, PageAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ClubRegistration, ClubRegistrationAdmin)
admin.site.register(SingleColumn, PageAdmin)
