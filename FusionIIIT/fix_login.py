import re

path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion-client/src/pages/login.jsx"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('localStorage.getItem("authToken")', 'localStorage.getItem("access")')
text = text.replace('const { token } = response.data;\n\n        localStorage.setItem("authToken", token);', 'const { access, refresh } = response.data;\n        localStorage.setItem("access", access);\n        localStorage.setItem("refresh", refresh);')

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
