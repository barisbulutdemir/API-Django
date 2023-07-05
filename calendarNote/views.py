from rest_framework import viewsets, decorators
from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from datetime import datetime
from django.shortcuts import get_list_or_404
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'created']
    search_fields = ['body', 'category__name']
    ordering_fields = ['created', 'updated']

    @decorators.action(detail=False, methods=['GET'])
    def getNotesByDate(self, request, year, month, day):
        date = datetime(year=int(year), month=int(month), day=int(day))
        notes = get_list_or_404(Note, created__date=date.date())
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
