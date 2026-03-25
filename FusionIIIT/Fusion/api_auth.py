from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class AuthMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        role_str = "student"
        try:
            role_str = str(user.extrainfo.user_type).lower()
        except:
            pass

        # Normalize roles so the frontend can reliably distinguish student vs faculty.
        # In this dataset, faculty users typically have user_type = 'staff'.
        if role_str == "staff":
            role_str = "faculty"

        # Give them comprehensive permissions so the sidebar populates fully for testing
        accessible_modules = {
            role_str: {
                "home": True,
                "online_cms": True,
                "course_registration": True,
                "program_and_curriculum": True,
                "mess_management": True,
                "visitor_hostel": True,
                "phc": True,
                "fts": True,
                "spacs": True,
                "complaint_management": True,
                "placement_cell": True,
                "department": True,
                "rspc": True,
                "inventory_management": True,
                "purchase_and_store": True,
                "hr": True,
                "examinations": True,
                "gymkhana": True,
                "iwd": True,
                "hostel_management": True,
                "other_academics": True,
                "course_management": True,
                "patent_management": True,
            }
        }
        
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': role_str,
            'roles': [role_str],
            'accessibleModules': accessible_modules
        })
