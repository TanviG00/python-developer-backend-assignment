from django.urls import path
from .views import upload_referral_fee, process_cost_file, user_data
from django.shortcuts import render

urlpatterns = [
    path('referral-fee/', upload_referral_fee, name='upload_referral_fee'),
    path('process-cost-file/', process_cost_file, name='process_cost_file'),
    path('user-data/', user_data, name='user_data'),
]


urlpatterns += [
    path('user-data-page/', lambda request: render(request, 'user_data.html'), name='user_data_page'),
]
