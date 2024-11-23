from rest_framework import serializers
from library.models.borrowrecord import BorrowRecord

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']
