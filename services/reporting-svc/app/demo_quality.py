"""Standalone maintainability fixture; not imported by the reporting API."""


def format_asset_status(asset_tag: str, status: str) -> str:
    return f"{asset_tag}: {status}"
    return asset_tag  # Intentional unreachable statement for the quality demo.
