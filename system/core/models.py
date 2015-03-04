#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys
import uuid

from PIL import Image
from django.conf import settings
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

logger = logging.getLogger(__name__)

class IgneousRockComposition(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Composition name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Composition description"))

    class Meta:
        verbose_name = _("Igneous Rock Composition")
        verbose_name_plural = _("Igneous Rock Compositions")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class IgneousRockMineralogy(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Mineralogy name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Mineralogy description"))

    class Meta:
        verbose_name = _("Igneous Rock Mineralogy")
        verbose_name_plural = _("Igneous Rock Mineralogies")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class IgneousRockColor(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Color name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Color description"))

    class Meta:
        verbose_name = _("Igneous Rock Color")
        verbose_name_plural = _("Igneous Rock Colors")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class IgneousRockOrigin(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Origin name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Origin description"))

    class Meta:
        verbose_name = _("Igneous Rock Origin")
        verbose_name_plural = _("Igneous Rock Origins")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class IgneousRockTexture(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Texture name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Texture description"))

    class Meta:
        verbose_name = _("Igneous Rock Texture")
        verbose_name_plural = _("Igneous Rock Textures")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class IgneousRockStructure(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Structure name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Structure description"))

    class Meta:
        verbose_name = _("Igneous Rock Structure")
        verbose_name_plural = _("Igneous Rock Structures")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRockOrigin(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Origin name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Origin description"))

    class Meta:
        verbose_name = _("Sedimentary Rock Origin")
        verbose_name_plural = _("Sedimentary Rock Origins")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRockGranularity(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Granularity name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Granularity description"))

    class Meta:
        verbose_name = _("Sedimentary Rock Granularity")
        verbose_name_plural = _("Sedimentary Rock Granularities")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRockFraction(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Fraction name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Fraction description"))

    class Meta:
        verbose_name = _("Sedimentary Rock Fraction")
        verbose_name_plural = _("Sedimentary Rock Fractions")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRockConstitution(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Constitution name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Constitution description"))

    class Meta:
        verbose_name = _("Sedimentary Rock Constitution")
        verbose_name_plural = _("Sedimentary Rock Constitutions")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRockStructure(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Structure name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Structure description"))

    class Meta:
        verbose_name = _("Sedimentary Rock Structure")
        verbose_name_plural = _("Sedimentary Rock Structures")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRockFormation(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Formation name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Formation description"))

    class Meta:
        verbose_name = _("Sedimentary Rock Formation")
        verbose_name_plural = _("Sedimentary Rock Formations")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class MetamorphicRockStructure(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Structure name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Structure description"))

    class Meta:
        verbose_name = _("Metamorphic Rock Structure")
        verbose_name_plural = _("Metamorphic Rock Structures")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class MetamorphicRockMineral(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Mineral name"))
    description = models.TextField(_("Description"), max_length=1024, blank=True, help_text=_("Mineral description"))

    class Meta:
        verbose_name = _("Metamorphic Rock Mineral")
        verbose_name_plural = _("Metamorphic Rock Minerals")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class Person(models.Model):
    name = models.CharField(_("Name"), max_length=64, help_text=_("Person name"))
    about = models.TextField(_("About"), max_length=256, blank=True, help_text=_("Person about"))
    email = models.EmailField(_("Email"), max_length=32, blank=True, help_text=_("Person email"))
    phone = models.CharField(_("Phone"), max_length=32, blank=True, help_text=_("Person phone"))

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def __unicode__(self):
        return "%s" % (self.name.capitalize())

class Rock(models.Model):
    name = models.CharField(_("Name"), max_length=256, help_text=_("Rock name"))
    description = models.TextField(_("Description"), max_length=10240, help_text=_("Description"))
    author = models.ForeignKey(Person, verbose_name=_("Author"), help_text=_("Author"))
    date = models.DateField(_("Date"), help_text=_("Date"))

    class Meta:
        verbose_name = _("Rock")
        verbose_name_plural = _("Rocks")

    def __unicode__(self):
        return u"%s" % (self.type.capitalize())

    def get_photos(self):
        return Photo.objects.filter(ROCK=self)

    def get_photo(self):
        return Photo.objects.filter(ROCK=self).order_by('?')[0].photo

class Photo(models.Model):
    rock = models.ForeignKey(Rock, related_name="photos")
    title = models.CharField(_("Title"), max_length=128, help_text=_("Photo title"))
    photo = ImageField(upload_to=settings.MEDIA_ROCKS_ROOT, max_length=256, help_text=_("Photo"))
    photographer = models.ForeignKey(Person, verbose_name=_("Photographer"), help_text=_("Rock photographer"), related_name="photo_photographer")

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __unicode__(self):
        return "%s" % (self.pk)


    def photo_tag(self):
        return "<img width='300' src='%s'>" % (self.photo.url)

    photo_tag.short_description = _("Current photo")
    photo_tag.allow_tags = True

class IgneousRock(Rock):
    composition = models.ForeignKey(IgneousRockComposition, verbose_name=_("Composition"), help_text=_("Igneous Rock Composition"))
    mineralogies = models.ManyToManyField(IgneousRockMineralogy, verbose_name=_("Mineralogies"), help_text=_("Igneous Rock Mineralogies"))
    color = models.ForeignKey(IgneousRockColor, verbose_name=_("Color"), help_text=_("Igneous Rock Color"))
    origin = models.ForeignKey(IgneousRockOrigin, verbose_name=_("Origin"), help_text=_("Igneous Rock Origin"))
    texture = models.ForeignKey(IgneousRockTexture, verbose_name=_("Texture"), help_text=_("Igneous Rock Texture"))
    structure = models.ForeignKey(IgneousRockStructure, verbose_name=_("Structure"), help_text=_("Igneous Rock Structure"))

    class Meta:
        verbose_name = _("Igneous Rock")
        verbose_name_plural = _("Igneous Rocks")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class SedimentaryRock(Rock):
    origin = models.ForeignKey(SedimentaryRockOrigin, verbose_name=_("Origin"), help_text=_("Sedimentary Rock Origin"))
    granularity = models.ForeignKey(SedimentaryRockGranularity, verbose_name=_("Granularity"), help_text=_("Sedimentary Rock Granularity"))
    fraction = models.ForeignKey(SedimentaryRockFraction, verbose_name=_("Fraction"), help_text=_("Sedimentary Rock Fraction"))
    constitution = models.ForeignKey(SedimentaryRockConstitution, verbose_name=_("Constitution"), help_text=_("Sedimentary Rock Constitution"))
    structure = models.ForeignKey(SedimentaryRockStructure, verbose_name=_("Structure"), help_text=_("Sedimentary Rock Structure"))
    formation = models.ForeignKey(SedimentaryRockFormation, verbose_name=_("Formation"), blank=True, help_text=_("Sedimentary Rock Formation"))

    class Meta:
        verbose_name = _("Sedimentary Rock")
        verbose_name_plural = _("Sedimentary Rocks")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())

class MetamorphicRock(Rock):
    structure = models.ForeignKey(MetamorphicRockStructure, verbose_name=_("Structure"), help_text=_("Metamorphic Rock Structure"))
    minerals = models.ManyToManyField(MetamorphicRockMineral, verbose_name=_("Minerals"), help_text=_("Metamorphic Rock Minerals"))

    class Meta:
        verbose_name = _("Metamorphic Rock")
        verbose_name_plural = _("Metamorphic Rocks")

    def __unicode__(self):
        return u"%s" % (self.name.capitalize())
