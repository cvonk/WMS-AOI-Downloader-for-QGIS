# -*- coding: utf-8 -*-
"""Basemap Tile Downloader – QGIS plugin entry point (WMS / WMTS / XYZ)."""


def classFactory(iface):
    from .plugin import BasemapTileDownloaderPlugin
    return BasemapTileDownloaderPlugin(iface)
