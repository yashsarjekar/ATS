from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from candidate.serializers import CandidateSerializer
from candidate.candidate_service.candidate_service import CandidateService
from candidate.objects.candidate_details import CandidateDetails
from rest_framework.exceptions import ValidationError
# Create your views here.

class CandidateView(APIView):

    def __init__(self):
        self.candidate_service = CandidateService()

    def post(self, request):
        try:
            candidate_serializer = CandidateSerializer(data=request.data)
            if candidate_serializer.is_valid(raise_exception=True):
                candidate_details = CandidateDetails(
                    name=request.data.get('name'),
                    age=request.data.get('age'),
                    gender=request.data.get('gender'),
                    email=request.data.get('email'),
                    phone_number=request.data.get('phone_number')
                )
                candidate_record = self.candidate_service.create_candidate(
                    candidate=candidate_details
                )
                if candidate_record:
                    response_dict = {
                        "meta": {
                            "message": "[INFO] Candidate Record is created",
                            "success": True,
                            "status": 200
                        },
                        "result": {
                            "id": candidate_record.get_id(),
                            "name": candidate_record.get_name(),
                            "email": candidate_record.get_email(),
                            "age": candidate_record.get_age(),
                            "gender": candidate_record.get_gender(),
                            "phone_number": candidate_record.get_phone_number()
                        }
                    }
                    return Response(response_dict)
                else:
                    response_dict = {
                        "meta": {
                            "message": "[INFO] Failed to create Candidate Record",
                            "success": False,
                            "status": 200
                        }
                    }
                    return Response(response_dict)
            response_dict = {
                "meta": {
                    "message": candidate_serializer.errors,
                    "success": False,
                    "status": 400
                }
            }  
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            response_dict = {
                "meta": {
                    "message": error.detail,
                    "success": False,
                    "status": 400
                }
            }
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            # Log the error or send error to sentry.
            response_dict = {
                "meta": {
                    "message": "Ops! Internal Server Error",
                    "success": False,
                    "status": 500
                }
            }
            return Response(response_dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request):
        try:
            candidate_details = CandidateDetails(
                name=request.data.get('name'),
                age=request.data.get('age'),
                gender=request.data.get('gender'),
                email=request.data.get('email'),
                phone_number=request.data.get('phone_number')
            )
            record_updated = self.candidate_service.update_candidate(
                candidate=candidate_details
            )
            if record_updated:
                response_dict = {
                    "meta": {
                        "message": "[INFO] Candidate Record is updated successfully",
                        "success": True,
                        "status": 200
                    }
                }
                return Response(response_dict)
            else:
                response_dict = {
                    "meta": {
                        "message": "[INFO] Failed to update Candidate Record",
                        "success": False,
                        "status": 200
                    }
                }
                return Response(response_dict)

        except Exception as error:
            # Log the error or send error to sentry.
            response_dict = {
                "meta": {
                    "message": "Ops! Internal Server Error",
                    "success": False,
                    "status": 500
                }
            }
            return Response(response_dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            email = request.data.get('email')
            is_deleted = self.candidate_service.delete_candidate(
                email=email
            )
            if is_deleted:
                response_dict = {
                    "meta": {
                        "message": "[INFO] Candidate Record is deleted successfully",
                        "success": True,
                        "status": 200
                    }
                }
                return Response(response_dict)
            else:
                response_dict = {
                    "meta": {
                        "message": "[INFO] Failed to delete Candidate Record",
                        "success": False,
                        "status": 200
                    }
                }
                return Response(response_dict)
        except Exception as error:
            # Log the error or send error to sentry.
            response_dict = {
                "meta": {
                    "message": "Ops! Internal Server Error",
                    "success": False,
                    "status": 500
                }
            }
            return Response(response_dict, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        