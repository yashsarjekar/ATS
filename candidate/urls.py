from django.urls import path
from candidate.views import (CandidateView, SearchCandidate)

urlpatterns = [
    path("api/v1/candidate", CandidateView.as_view()),
    path("api/v1/search", SearchCandidate.as_view())
]