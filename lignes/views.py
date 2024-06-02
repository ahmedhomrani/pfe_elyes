from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Ligne, Test, LigneTest, Banc
from .serializers import (
    BancForLigneTestSerializer, LigneCreateSerializer, LigneForTestSerializer, LigneTestForLigneSerializer, LigneUpdateSerializer, LigneRetrieveSerializer, LigneDetailSerializer, LigneListSerializer,
    TestCreateSerializer, TestUpdateSerializer, TestRetrieveSerializer, TestListSerializer,
    LigneTestCreateSerializer, LigneTestRetrieveSerializer, LigneTestListSerializer,
    BancCreateSerializer, BancRetrieveSerializer, BancListSerializer
)

# Ligne Views
class LigneTestsByLigneAPIView(generics.ListAPIView):
    serializer_class = LigneTestForLigneSerializer

    def get_queryset(self):
        ligne_id = self.kwargs['pk']
        return LigneTest.objects.filter(ligne_id=ligne_id)
class BancsByLigneTestAPIView(generics.ListAPIView):
    serializer_class = BancForLigneTestSerializer

    def get_queryset(self):
        ligne_test_id = self.kwargs['pk']
        return Banc.objects.filter(ligne_test_id=ligne_test_id)
class LignesByTestAPIView(generics.ListAPIView):
    serializer_class = LigneForTestSerializer

    def get_queryset(self):
        test_id = self.kwargs['pk']
        return LigneTest.objects.filter(test_id=test_id)    

class LigneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ligne.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LigneCreateSerializer
        return LigneListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LigneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LigneDetailSerializer
        return LigneUpdateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Test Views
class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TestCreateSerializer
        return TestListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TestRetrieveSerializer
        return TestUpdateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# LigneTest Views
class LigneTestListCreateAPIView(generics.ListCreateAPIView):
    queryset = LigneTest.objects.all()
    serializer_class = LigneTestListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LigneTestCreateSerializer
        return LigneTestListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LigneTestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LigneTest.objects.all()
    serializer_class = LigneTestRetrieveSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LigneTestRetrieveSerializer
        return LigneTestCreateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Banc Views
class BancListCreateAPIView(generics.ListCreateAPIView):
    queryset = Banc.objects.all()
    serializer_class = BancListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BancCreateSerializer
        return BancListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BancRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banc.objects.all()
    serializer_class = BancRetrieveSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BancRetrieveSerializer
        return BancCreateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.http import HttpResponse
from django .http import FileResponse
import io 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.platypus import Image
from .models import Ligne , Test, Banc, LigneTest
from django.views import View

class GeneratePDFLigne(View):
    def get(self, request, *args, **kwargs):
        # Query all lignes from the database
        lignes = Ligne.objects.all()

        # Create a buffer for the PDF
        buffer = io.BytesIO()

        # Create a PDF document
        pdf = SimpleDocTemplate(buffer, pagesize=letter)

        # Define data for the table
        data = [['ID', 'Title', 'Date Creation', 'Status', 'Semaine']]
        for ligne in lignes:
            data.append([str(ligne.id), ligne.title, str(ligne.datecreation), ligne.status, ligne.sem])

        # Create a table and style
        table = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # Apply style to the table
        table.setStyle(style)

        # Add the table to the PDF document
        elements = []
        elements.append(table)
        pdf.build(elements)

        # Get the value of the buffer
        pdf_buffer = buffer.getvalue()
        buffer.close()

        # Create an HTTP response with the PDF as attachment
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="lignes.pdf"'
        response.write(pdf_buffer)

        return response

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        # Query all lignes from the database
        lignes = Ligne.objects.all()

        # Create a buffer for the PDF
        buffer = io.BytesIO()

        # Create a PDF document
        pdf = SimpleDocTemplate(buffer, pagesize=landscape(letter))

        # Create a stylesheet
        styles = getSampleStyleSheet()
        elements = []

        for ligne in lignes:
            # Add the name of the ligne
            elements.append(Paragraph(f"Ligne: {ligne.title}", styles['Heading1']))
            elements.append(Spacer(1, 12))

            # Add the list of tests assigned to the ligne
            ligne_tests = LigneTest.objects.filter(ligne=ligne)
            if ligne_tests.exists():
                for ligne_test in ligne_tests:
                    test = ligne_test.test
                    elements.append(Paragraph(f"Test: {test.name}", styles['Heading2']))
                    
                    # Add the list of bancs assigned to the test
                    bancs = Banc.objects.filter(ligne_test=ligne_test)
                    if bancs.exists():
                        banc_data = [['Banc Name', 'Technician', 'Validator', 'Validation Date', 'Revalidation Date', 'Validation Status', 'Comment']]
                        for banc in bancs:
                            banc_data.append([
                                banc.banc_name, 
                                str(banc.technician) if banc.technician else "N/A",
                                str(banc.validator) if banc.validator else "N/A",
                                str(banc.validation_date) if banc.validation_date else "N/A",
                                str(banc.revalidation_date) if banc.revalidation_date else "N/A",
                                'Validated' if banc.validated_by_technician else 'Not Validated',
                                banc.comment if banc.comment else ""
                            ])
                        
                        banc_table = Table(banc_data)
                        banc_table.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ]))
                        elements.append(banc_table)
                        elements.append(Spacer(1, 12))
                    else:
                        elements.append(Paragraph("No Bancs Assigned.", styles['BodyText']))
                        elements.append(Spacer(1, 12))
            else:
                elements.append(Paragraph("No Tests Assigned.", styles['BodyText']))
                elements.append(Spacer(1, 12))

        # Build the PDF
        pdf.build(elements)

        # Get the value of the buffer
        pdf_buffer = buffer.getvalue()
        buffer.close()

        # Create an HTTP response with the PDF as attachment
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="lignesTest.pdf"'
        response.write(pdf_buffer)

        return response