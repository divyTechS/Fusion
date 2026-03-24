from django.contrib.auth.models import User

# Superuser
su = User.objects.filter(is_superuser=True).first()
if su:
    su.set_password('fusion123')
    su.save()
    print("Superuser:", su.username)

# Normal user
reg = User.objects.filter(is_superuser=False).first()
if reg:
    reg.set_password('fusion123')
    reg.save()
    print("Normal user:", reg.username)

