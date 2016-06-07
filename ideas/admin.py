from django.contrib import admin
from .models import Hackathon, Team, TeamMember, TeamIdea, TeamSubmission
# Register your models here.

# Register your models here.
admin.site.register(Hackathon)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(TeamIdea)
admin.site.register(TeamSubmission)