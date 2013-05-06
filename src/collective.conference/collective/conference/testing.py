# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from zope.configuration import xmlconfig

class CollectiveConference(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.conference
        xmlconfig.file('configure.zcml',
            collective.conference,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.conference:default')

COLLECTIVE_CONFERENCE_FIXTURE = CollectiveConference()
COLLECTIVE_CONFERENCE_INTEGRATION_TESTING = IntegrationTesting(
        bases=(COLLECTIVE_CONFERENCE_FIXTURE,),
        name="Collective:Integration"
        )

