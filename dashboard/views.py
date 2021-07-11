from django.shortcuts import render
from houseservices.models import HouseServices


# Create your views here.
def dashboard_main(request):

  query_params = request.GET.get('month', None)

  jan_num_services = HouseServices.objects.filter(created_at__month=1).count()
  fev_num_services = HouseServices.objects.filter(created_at__month=2).count()
  mar_num_services = HouseServices.objects.filter(created_at__month=3).count()
  abr_num_services = HouseServices.objects.filter(created_at__month=4).count()
  mai_num_services = HouseServices.objects.filter(created_at__month=5).count()

  data = [
      jan_num_services, fev_num_services, mar_num_services, abr_num_services,
      mai_num_services
  ]

  max_data = max(data)
  for i in range(max_data - 10, max_data + 11):
    if i % 10 == 0:
      max_data = i

  context = {
      "count_all_services_by_month": data,
      "max_data": max_data,
      "labels": ["jan", "fev", "mar", "abr", "may"]
  }
  return render(request, 'dashboard.html', context)
