from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import (
    ReviewSerializer, LocationSerializer, DeviceSerializer,
    TypeSerializer,
)
from reviews.models import Review
from management.models import Device, Location, Type


class ReviewList(APIView):
    """
    List all reviews, or create a new review.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response({'arows': serializer.data})

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    """
    Retrieve, update review instance.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationList(APIView):
    """
    List all locations, or create a new review.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response({'arows': serializer.data})

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetail(APIView):
    """
    Retrieve, update location instance.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceList(APIView):
    """
    List all devices, or create a new review.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response({'arows': serializer.data})

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDetail(APIView):
    """
    Retrieve, update device instance.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeList(APIView):
    """
    List all types, or create a new review.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response({'arows': serializer.data})

    def post(self, request, format=None):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeDetail(APIView):
    """
    Retrieve, update type instance.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Type.objects.get(pk=pk)
        except Type.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = TypeSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = TypeSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
