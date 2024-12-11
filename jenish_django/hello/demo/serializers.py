from rest_framework import serializers
from.models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

        def validation(self,data):

        #  NAME VALIDATION 
            if not data["name"].isalpha():
                raise serializers.ValidationError("name must contain only letter")
        
        # AGE VALIDATION 
            if data['age'] < 18 :
               raise serializers.ValidationError("The person has to be at least 18 year old")
        

        #  EMAIL VALIDATION

            email=data.get("EMAIL")
            if data ["EMAIL"] == '@gmail.com':
                raise serializers.ValidationError("Email Is Not Valid")
        
            elif email [0].isdigit():
                raise serializers.ValidationError("Email Is Not Valid")
        
            elif not email.islower():
                raise serializers.ValidationError("Email Is Not Valid")
        
            elif not email.endswitch('@gmail.com'):
                raise serializers.ValidationError("Email Is Not Valid")
        

        #  MOBILE NUMBER VALIDATION 

            Mobile=data.get('Number')
            if len(Mobile) != 10 or not Mobile.isdigit():
                raise serializers.ValidationError("Number Is Not Validation ")
       
    
        #  PASSWORD VALIDATION

            if data ['password'] != data ["correctpassword"]:
                raise serializers.ValidationError('Password Is Wrong')
            return data