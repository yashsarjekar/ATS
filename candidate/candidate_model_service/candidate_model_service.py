from candidate.models import Candidate
from candidate.objects.candidate_details import CandidateDetails
from candidate.objects.candidate_already_exist_exception import CandidateAlreadyExist

class CandidateModelService:

    def create_candidate(self, candidate: CandidateDetails):
        record = Candidate.objects.filter(email=candidate.get_email())
        if len(record) == 1:
            raise CandidateAlreadyExist(
                f"Candidate Already exist with email {candidate.get_email()}"
            )
        candidate = Candidate.objects.create(
            name=candidate.get_name(),
            age=candidate.get_age(),
            email=candidate.get_email(),
            gender=candidate.get_gender(),
            phone_number=candidate.get_phone_number()
        )
        return candidate
    
    def update_candidate(self, candidate: CandidateDetails):
        update_flag = False
        try:
            Candidate.objects.filter(email=candidate.get_email()).update(
                name=candidate.get_name(),
                age=candidate.get_age(),
                gender=candidate.get_gender(),
                phone_number=candidate.get_phone_number()
            )
            update_flag = True
        except Exception as error:
            # send exception the exception to sentry
            update_flag = False
        return update_flag
    
    def delete_candidate(self, email):
        is_deleted = False
        try:
            Candidate.objects.filter(email=email).delete()
            is_deleted = True
        except Exception as error:
            # send exception to sentry
            is_deleted = False
        
        return is_deleted