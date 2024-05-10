from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework import serializers
from ModelApi.models import Company



# ===============================
# serializers Use Start
# ===============================
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields= "__all__"
# ===============================
# serializers Use End
# ===============================



# ===============================
# viewsets Use End
# ===============================
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
# ===============================
# viewsets Use End
# ===============================




# ===============================
# Router Name Register => companies
# ===============================
from django.urls import path,include
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)


urlpatterns = [
    path('',include(router.urls))
]
# =====ENd==========================
# Router Name Register => companies 
# =====ENd==========================
