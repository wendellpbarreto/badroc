#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from redactor.widgets import RedactorEditor
from django.db import models

from .models import (
    IgneousRock,
    SedimentaryRock,
    MetamorphicRock,
)

class IgneousRockAdminForm(forms.ModelForm):
    class Meta:
        model = IgneousRock
        widgets = {
            "description": RedactorEditor(),
        }

class SedimentaryRockAdminForm(forms.ModelForm):
    class Meta:
        model = SedimentaryRock
        widgets = {
            "description": RedactorEditor(),
        }

class MetamorphicRockAdminForm(forms.ModelForm):
    class Meta:
        model = MetamorphicRock
        widgets = {
            "description": RedactorEditor(),
        }

# class MemberAdminForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         widgets = {
#             "about": RedactorEditor(),
#         }

# class AuthorAdminForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         widgets = {
#             "about": RedactorEditor(),
#         }

# class PhotographerAdminForm(forms.ModelForm):
#     class Meta:
#         model = Photographer
#         widgets = {
#             "about": RedactorEditor(),
#         }

# class NoticeAdminForm(forms.ModelForm):
#     class Meta:
#         model = Notice
#         widgets = {
#             "body": RedactorEditor(),
#         }

# class PhotogalleryAdminForm(forms.ModelForm):
#     class Meta:
#         model = Photogallery
#         widgets = {
#             "body": RedactorEditor(),
#         }

# class VideoLibraryAdminForm(forms.ModelForm):
#     class Meta:
#         model = VideoLibrary
#         widgets = {
#             "body": RedactorEditor(),
#         }

# class PodcastAdminForm(forms.ModelForm):
#     class Meta:
#         model = Podcast
#         widgets = {
#             "body": RedactorEditor(),
#         }

# class EventAdminForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         formfield_overrides = {
#             models.ManyToManyField: {"widget": forms.CheckboxSelectMultiple},
#         }
#         widgets = {
#             "body": RedactorEditor(),
#         }
