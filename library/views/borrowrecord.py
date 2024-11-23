from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from library.models.borrowrecord import BorrowRecord
from library.serializers.borrowrecord import BorrowRecordSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def get_permissions(self):
        return [IsAuthenticated()]
