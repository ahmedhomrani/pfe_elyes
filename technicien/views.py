# from rest_framework.response import Response
# from rest_framework import generics
# from account.permissions import IsAdminUser
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsTechnician
# from lignesAssignTo.models import LignesAssignto
# from technicien.serializers import LignesAssigntoUpdateSerializer

# class YourTechnicianView(generics.RetrieveUpdateAPIView):
#     permission_classes = [IsAdminUser]
#     # Your view implementation

# class LignesAssigntoUpdateAPIView(generics.UpdateAPIView):
#     queryset = LignesAssignto.objects.all()
#     serializer_class = LignesAssigntoUpdateSerializer
#     permission_classes = [IsAuthenticated, IsTechnician]  # Add IsAuthenticated for token validation

#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from lignesAssignTo.models import LignesAssignto
# from lignesAssignTo.serializers import LignesAssigntoSerializer
# from account.permissions import IsTechnician  

# class TechnicianLignesAssigntoListAPIView(generics.ListAPIView):
#     serializer_class = LignesAssigntoSerializer
#     permission_classes = [IsAuthenticated, IsTechnician]

#     def get_queryset(self):
#         technician_id = self.request.user.id
#         return LignesAssignto.objects.filter(technician=technician_id)

