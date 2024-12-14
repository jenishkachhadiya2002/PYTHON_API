from rest_framework import serializers
from.models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate(self,data):

        #  NAME VALIDATION 
        if not data["Name"].isalpha():
            raise serializers.ValidationError("name must contain only letter")
        
        # AGE VALIDATION 
        if data['Age'] < 18 :
            raise serializers.ValidationError("The person has to be at least 18 year old")
        

        #  EMAIL VALIDATION

        email=data.get("Email")
        if data ["Email"] == '@gmail.com':
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

        if data['Password'] != data["Confirm_Password"]:
            raise serializers.ValidationError('Password Is Wrong')
        return data