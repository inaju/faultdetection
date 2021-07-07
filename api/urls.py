from django.urls import path, include
from .views import ErrorCodeList, ErrorCodeListDetail
urlpatterns = [
    path('get/', ErrorCodeList.as_view(), name="error_code_list"),
    path('get/<int:uid>', ErrorCodeListDetail.as_view(),
         name="error_code_list_detail"),
    path('post/', ErrorCodeList.as_view()),

]
