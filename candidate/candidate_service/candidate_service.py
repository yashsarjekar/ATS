from candidate.candidate_model_service.candidate_model_service import CandidateModelService
from candidate.objects.candidate_details import CandidateDetails
from candidate.objects.candidate_record import CandidateRecord

class CandidateService:

    def __init__(self) -> None:
        self.candidate_model_service = CandidateModelService()

    def create_candidate(self, candidate: CandidateDetails):
        record = self.candidate_model_service.create_candidate(
            candidate=candidate
        )
        return CandidateRecord(
            id=record.id,
            name=record.name,
            age=record.age,
            email=record.email,
            phone_number=record.phone_number,
            gender=record.gender
        )
    
    def update_candidate(self, candidate: CandidateDetails):
        updated = self.candidate_model_service.update_candidate(
            candidate=candidate
        )
        return updated
    
    def delete_candidate(self, email):
        is_deleted = self.candidate_model_service.delete_candidate(
            email=email
        )
        return is_deleted
    
    def search_candidates(self, words):
        candidates = []
        records = self.candidate_model_service.search_candidates(words=words)

        for record in records:
            candidates.append(
                CandidateRecord(
                    id=record.id,
                    name=record.name,
                    age=record.age,
                    email=record.email,
                    phone_number=record.phone_number,
                    gender=record.gender
                )
            )
        return candidates