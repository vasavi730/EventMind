from rest_framework import serializers
from .models import DashBoard
class RecordSerializer(serializers.ModelSerializer):
	class Meta:
		model=DashBoard
		fields=('client_id','client_name','client_email','client_mobile','client_address','client_event','client_status')