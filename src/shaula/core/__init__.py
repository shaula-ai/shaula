"""Shared helpers for the shaula namespace."""

from importlib.metadata import PackageNotFoundError, version

DISTRIBUTION_NAME = "shaula-ai"

try:
    __version__ = version(DISTRIBUTION_NAME)
except PackageNotFoundError:
    __version__ = "0.0.0"
