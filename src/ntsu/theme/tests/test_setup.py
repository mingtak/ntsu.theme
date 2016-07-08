# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ntsu.theme.testing import NTSU_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ntsu.theme is properly installed."""

    layer = NTSU_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ntsu.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ntsu.theme'))

    def test_browserlayer(self):
        """Test that INtsuThemeLayer is registered."""
        from ntsu.theme.interfaces import (
            INtsuThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(INtsuThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NTSU_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ntsu.theme'])

    def test_product_uninstalled(self):
        """Test if ntsu.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ntsu.theme'))

    def test_browserlayer_removed(self):
        """Test that INtsuThemeLayer is removed."""
        from ntsu.theme.interfaces import INtsuThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(INtsuThemeLayer, utils.registered_layers())
