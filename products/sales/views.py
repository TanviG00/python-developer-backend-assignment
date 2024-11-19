import os
import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from django.conf import settings
from django.http import JsonResponse

def upload_referral_fee(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return redirect('process_cost_file')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form, 'title': 'Upload Referral Fee File'})


def process_cost_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            cost_file = request.FILES['file']
            referral_fee_path = os.path.join(settings.MEDIA_ROOT, os.listdir(settings.MEDIA_ROOT)[0])

            # Load the files
            referral_fee_df = pd.read_excel(referral_fee_path)
            cost_df = pd.read_excel(cost_file)

            merged_df = pd.merge(cost_df, referral_fee_df, on="Product Name", how="inner")
            merged_df['Total Cost'] = merged_df['Cost'] * merged_df['Referral Fees']

            output_path = os.path.join(settings.MEDIA_ROOT, 'processed_file.xlsx')
            merged_df.to_excel(output_path, index=False)

            with open(output_path, 'rb') as f:
                response = HttpResponse(f, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="processed_file.xlsx"'
                return response
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form, 'title': 'Upload Cost File'})




def user_data(request):
    processed_file_path = os.path.join(settings.MEDIA_ROOT, 'processed_file.xlsx')
    
    if not os.path.exists(processed_file_path):
        return JsonResponse({'error': 'No processed file found. Please upload and process files first.'}, status=400)

    # Load the processed Excel file
    data_df = pd.read_excel(processed_file_path)

    # Calculate total sales and product-specific sales
    total_sales = float(data_df['Total Cost'].sum())  # Convert to standard Python float
    product_sales = {product: float(sales) for product, sales in data_df.groupby('Product Name')['Total Cost'].sum().items()}

    return JsonResponse({
        'total_sales': total_sales,
        'product_sales': product_sales,
    })

