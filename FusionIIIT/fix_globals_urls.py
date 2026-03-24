import re

path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion/FusionIIIT/applications/globals/api/urls.py"
with open(path, "r") as f:
    content = f.read()

# Instead of "auth/me", let's map it to views.profile or create a simple view
# React expects auth/me to validate token and return user details.

if "auth/me" not in content:
    content = content.replace("urlpatterns = [", "urlpatterns = [\n    url(r'^auth/me/', views.profile, name='me-api'),")
    with open(path, "w") as f:
        f.write(content)
