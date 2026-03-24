import re

path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion/FusionIIIT/Fusion/urls.py"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# I am creating an api_auth view inside globals because it is simpler, or just create it in the same file.
# But wait, we should do it properly. Let's create an auth API view inside global's views or a new file `api_auth.py` in Fusion config.

text = text.replace("from django.contrib.auth import views as auth_views", 
"from django.contrib.auth import views as auth_views\nfrom . import api_auth")

api_patterns = """
    # API AUTH
    url(r'^api/auth/login/$', api_auth.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', api_auth.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/auth/me/$', api_auth.AuthMeView.as_view(), name='api_auth_me'),
"""

if "api/auth/login/" not in text:
    text = text.replace("urlpatterns = [", "urlpatterns = [" + api_patterns)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
