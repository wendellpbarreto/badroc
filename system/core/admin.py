#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *

admin.site.unregister(Group)

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    can_delete = True
    max_num = 99
    classes = ("grp-collapse grp-open",)
    inline_classes = ("grp-collapse grp-open",)
    readonly_fields = ("photo_tag",)

class IgneousRockAdmin(admin.ModelAdmin):
    model = IgneousRock
    form = IgneousRockAdminForm
    inlines = (PhotoInline,)
    classes = ("grp-collapse grp-open",)
    inline_classes = ("grp-collapse grp-open",)
    fieldsets = (
        (
            _("Informations"), {
                "fields" : (
                    "name",
                    ("composition", "color"),
                    ("origin", "texture"),
                    "structure", "mineralogies", "description",
                )
            }
        ),
        (
             _("Datation"), {
                "fields" : (
                    ("author", "date"),
                )
            }
        ),
    )
    list_display = ("name",)
    list_filter = ("composition", "color", "origin", "texture")
    search_fields = ("composition", "color", "origin", "texture")
    ordering = ("name",)

admin.site.register(IgneousRock, IgneousRockAdmin)

class SedimentaryRockAdmin(admin.ModelAdmin):
    model = SedimentaryRock
    form = SedimentaryRockAdminForm
    inlines = (PhotoInline,)
    classes = ("grp-collapse grp-open",)
    inline_classes = ("grp-collapse grp-open",)
    fieldsets = (
        (
            _("Informations"), {
                "fields" : (
                    "name",
                    ("origin", "granularity"),
                    ("fraction", "constitution"),
                    ("structure", "formation"),
                    "description",
                )
            }
        ),
        (
             _("Datation"), {
                "fields" : (
                    ("author", "date"),
                )
            }
        ),
    )
    list_display = ("name",)
    list_filter = ("origin", "granularity", "fraction", "constitution", "structure", "formation")
    search_fields = ("origin", "granularity", "fraction", "constitution", "structure", "formation")
    ordering = ("name",)

admin.site.register(SedimentaryRock, SedimentaryRockAdmin)

class MetamorphicRockAdmin(admin.ModelAdmin):
    model = MetamorphicRock
    form = MetamorphicRockAdminForm
    inlines = (PhotoInline,)
    classes = ("grp-collapse grp-open",)
    inline_classes = ("grp-collapse grp-open",)
    fieldsets = (
        (
            _("Informations"), {
                "fields" : (
                    "name",
                    ("minerals", "structure"),
                    "description",
                )
            }
        ),
        (
             _("Datation"), {
                "fields" : (
                    ("author", "date"),
                )
            }
        ),
    )
    list_display = ("name",)
    list_filter = ("structure",)
    search_fields = ("structure",)
    ordering = ("name",)

admin.site.register(MetamorphicRock, MetamorphicRockAdmin)

class PersonAdmin(admin.ModelAdmin):
    model = Person

admin.site.register(Person, PersonAdmin)

class IgneousRockCompositionAdmin(admin.ModelAdmin):
    model = IgneousRockComposition

admin.site.register(IgneousRockComposition, IgneousRockCompositionAdmin)

class IgneousRockMineralogyAdmin(admin.ModelAdmin):
    model = IgneousRockMineralogy

admin.site.register(IgneousRockMineralogy, IgneousRockMineralogyAdmin)

class IgneousRockColorAdmin(admin.ModelAdmin):
    model = IgneousRockColor

admin.site.register(IgneousRockColor, IgneousRockColorAdmin)

class IgneousRockOriginAdmin(admin.ModelAdmin):
    model = IgneousRockOrigin

admin.site.register(IgneousRockOrigin, IgneousRockOriginAdmin)

class IgneousRockTexturedmin(admin.ModelAdmin):
    model = IgneousRockTexture

admin.site.register(IgneousRockTexture, IgneousRockTexturedmin)

class IgneousRockStructureAdmin(admin.ModelAdmin):
    model = IgneousRockStructure

admin.site.register(IgneousRockStructure, IgneousRockStructureAdmin)

class SedimentaryRockOriginAdmin(admin.ModelAdmin):
    model = SedimentaryRockOrigin

admin.site.register(SedimentaryRockOrigin, SedimentaryRockOriginAdmin)

class SedimentaryRockGranularityAdmin(admin.ModelAdmin):
    model = SedimentaryRockGranularity

admin.site.register(SedimentaryRockGranularity, SedimentaryRockGranularityAdmin)

class SedimentaryRockFractionAdmin(admin.ModelAdmin):
    model = SedimentaryRockFraction

admin.site.register(SedimentaryRockFraction, SedimentaryRockFractionAdmin)

class SedimentaryRockConstitutionAdmin(admin.ModelAdmin):
    model = SedimentaryRockConstitution

admin.site.register(SedimentaryRockConstitution, SedimentaryRockConstitutionAdmin)

class SedimentaryRockStructureAdmin(admin.ModelAdmin):
    model = SedimentaryRockStructure

admin.site.register(SedimentaryRockStructure, SedimentaryRockStructureAdmin)

class SedimentaryRockFormationAdmin(admin.ModelAdmin):
    model = SedimentaryRockFormation

admin.site.register(SedimentaryRockFormation, SedimentaryRockFormationAdmin)

class MetamorphicRockStructureAdmin(admin.ModelAdmin):
    model = MetamorphicRockStructure

admin.site.register(MetamorphicRockStructure, MetamorphicRockStructureAdmin)

class MetamorphicRockMineralAdmin(admin.ModelAdmin):
    model = MetamorphicRockMineral

admin.site.register(MetamorphicRockMineral, MetamorphicRockMineralAdmin)