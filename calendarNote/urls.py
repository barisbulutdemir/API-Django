from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('notes/getNotesByDate/<int:year>/<int:month>/<int:day>/', NoteViewSet.as_view({'get': 'getNotesByDate'}), name='get_notes_by_date'),
]
