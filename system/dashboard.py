"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'rochas.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.AppList(
            _('Rocks'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=(
                'system.core.models.IgneousRock',
                'system.core.models.SedimentaryRock',
                'system.core.models.MetamorphicRock',
            ),

        ))

        self.children.append(modules.Group(
            _('Administration'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('General configurations'),
                    collapsible=False,
                    column=1,
                    models=(
                        'system.core.models.Person',
                    ),
                ),
                modules.AppList(
                    _('Igneous Rocks'),
                    collapsible=False,
                    column=1,
                    models=(
                        'system.core.models.IgneousRockColor',
                        'system.core.models.IgneousRockComposition',
                        'system.core.models.IgneousRockMineralogy',
                        'system.core.models.IgneousRockOrigin',
                        'system.core.models.IgneousRockStructure',
                        'system.core.models.IgneousRockTexture',
                    ),
                ),
                modules.AppList(
                    _('Metamorphic Rocks'),
                    collapsible=False,
                    column=1,
                    models=(
                        'system.core.models.MetamorphicRockStructure',
                        'system.core.models.MetamorphicRockMineral',
                    ),
                ),
                modules.AppList(
                    _('Sedimentary Rocks'),
                    collapsible=False,
                    column=1,
                    models=(
                        'system.core.models.SedimentaryRockOrigin',
                        'system.core.models.SedimentaryRockGranularity',
                        'system.core.models.SedimentaryRockFraction',
                        'system.core.models.SedimentaryRockConstitution',
                        'system.core.models.SedimentaryRockStructure',
                        'system.core.models.SedimentaryRockFormation',
                    ),
                ),
            ]
        ))

        self.children.append(modules.LinkList(
            _('Pages'),
            column=2,
            children=[
                {
                    'title': _('rochas GUI'),
                    'url': '/home/',
                    'external': False,
                },
                # {
                #     'title': _('Grappelli Documentation'),
                #     'url': 'http://packages.python.org/django-grappelli/',
                #     'external': True,
                # },
                # {
                #     'title': _('Grappelli Google-Code'),
                #     'url': 'http://code.google.com/p/django-grappelli/',
                #     'external': True,
                # },
            ]
        ))

        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            column=2,
            collapsible=False,
            limit=5,
        ))



