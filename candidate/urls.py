from django.urls import path
from candidate.views import CandidateView

urlpatterns = [
    path("api/v1/candidate", CandidateView.as_view()),
]