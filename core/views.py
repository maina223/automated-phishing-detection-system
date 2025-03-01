from django.shortcuts import render
from .models import EmailRecord  # Import EmailRecord model
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    phishing_reports = EmailRecord.objects.all().order_by('-timestamp')  # Fetch records
    return render(request, 'dashboard.html', {'phishing_reports': phishing_reports})
