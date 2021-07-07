from django.shortcuts import render
from rest_framework import generics
from .models import ErrorCodeModel
from .serializers import ErrorCodeSerializer


class ErrorCodeList(generics.ListCreateAPIView):
    queryset = ErrorCodeModel.objects.all()
    serializer_class = ErrorCodeSerializer


class ErrorCodeListDetail(generics.ListAPIView):

    # queryset = ErrorCodeModel.objects.all()
    # serializer_class = ErrorCodeSerializer

    def get_queryset(self):

        queryset = ErrorCodeModel.objects.filter(uid=self.kwargs["uid"])
        return queryset
    serializer_class = ErrorCodeSerializer


# class PollDetail(generics.RetrieveDestroyAPIView):


# queryset = Poll.objects.all()
# serializer_class = PollSerializer
