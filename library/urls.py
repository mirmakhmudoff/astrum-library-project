from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, BorrowRecordViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('borrow', BorrowRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
