# -*- coding: utf-8 -*-

import unittest2 as unittest
from collective.conference.testing import COLLECTIVE_CONFERENCE_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName
from plone import api

class TestSetup(unittest.TestCase):
    layer = COLLECTIVE_CONFERENCE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        '''Teste de instalação do produto.'''
        installer = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('collective.conference'))

    def test_uninstall(self):
        """Test if tutorial.todoapp is cleanly uninstalled."""
        installer = getattr(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.conference'])
        self.assertFalse(installer.isProductInstalled('collective.conference'))

    # metadata.xml
    def test_dependencies_installed(self):
        """Test that all dependencies are installed."""
        installer = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))

    # types/person.xml
    def test_person_installed(self):
        """Test that person content type is listed in portal_types."""
        types = getattr(self.portal, 'portal_types')
        self.assertIn('person', types.objectIds())

'''
    def test_add_person(self):
        """Test that we can add a Person."""
        api.content.create(
            container=self.portal,
            type="person",
            title=u"Magneto",
            e_mail=u"magneto@marvel.com",
        )
        self.assertEquals(self.folder['magneto'].title, u'Magneto')
'''
