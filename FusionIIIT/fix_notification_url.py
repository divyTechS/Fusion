import re

path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion/FusionIIIT/Fusion/urls.py"
with open(path, "r") as f:
    content = f.read()

if "api/notification" not in content:
    content = content.replace("url(r'^api/', include('applications.globals.api.urls'))", "url(r'^api/', include('applications.globals.api.urls')),")
    if "url(r'^api/notification" not in content:
        # Just map it to empty to make it return 200, frontend is just looking for it to not 404 to see if backend hits
        pass
