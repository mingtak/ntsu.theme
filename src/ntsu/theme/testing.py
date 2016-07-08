# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ntsu.theme


class NtsuThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=ntsu.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ntsu.theme:default')


NTSU_THEME_FIXTURE = NtsuThemeLayer()


NTSU_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NTSU_THEME_FIXTURE,),
    name='NtsuThemeLayer:IntegrationTesting'
)


NTSU_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NTSU_THEME_FIXTURE,),
    name='NtsuThemeLayer:FunctionalTesting'
)


NTSU_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NTSU_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='NtsuThemeLayer:AcceptanceTesting'
)
