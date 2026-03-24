"""
This module previously contained a one-off helper script that edited
``applications/globals/api/urls.py`` via a hard-coded, absolute local path.

Such scripts are environment-specific and must not be committed to the
repository because they can unexpectedly mutate project files when run
in other environments (e.g., CI or other developers' machines).

The implementation has been intentionally removed. If you need to update
URL patterns, do so directly in the Django project or via a proper
management command or migration script.
"""

if __name__ == "__main__":
    raise SystemExit(
        "This helper script is intentionally disabled and should not be "
        "used from the repository. Update URL patterns directly in the "
        "Django project instead."
    )
