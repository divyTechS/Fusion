path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion/FusionIIIT/applications/globals/api/views.py"
with open(path, "r") as f:
    content = f.read()

if "def NotificationRead" not in content:
    with open(path, "a") as f:
        f.write("\n@api_view(['GET', 'POST'])\n@authentication_classes([TokenAuthentication])\n@permission_classes([IsAuthenticated])\ndef NotificationRead(request):\n    return Response({'unread_count': 0, 'notifications': []}, status=200)\n")
