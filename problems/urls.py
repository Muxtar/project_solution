from django.urls import path
from problems.views import problems, problemDetail, groups

urlpatterns = [
    path('', problems, name='problems'),
    path('problem/', problems, name='problem'),
    path('problemDetail/<int:pk>/', problemDetail, name='problemdetail'),
    path('groups/', groups)
]