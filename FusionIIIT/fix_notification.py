import re

path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion/FusionIIIT/applications/globals/api/urls.py"
with open(path, "r") as f:
    content = f.read()

if "api/notification" not in content:
    content = content.replace("urlpatterns = [", "urlpatterns = [\n    url(r'^notification/$', views.NotificationRead, name='dummy_notifs'),\n    url(r'^auth/me$', views.profile, name='me-api-2'),\n")
    with open(path, "w") as f:
        f.write(content)
