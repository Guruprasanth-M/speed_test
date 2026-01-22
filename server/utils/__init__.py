"""
Utility functions for the Speedtest server.

This package contains reusable, side-effect-free helpers
that can be safely imported by:
- API routes
- Services
- CLI tools
"""

from .get_ip import (
    get_hostname,
    get_local_ip,
    get_public_ip,
    get_ip_info,
)

__all__ = [
    "get_hostname",
    "get_local_ip",
    "get_public_ip",
    "get_ip_info",
]
