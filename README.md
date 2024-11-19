Features
File Upload:
Referral fee file and cost file can be uploaded through separate pages.
Uploaded files are saved in the media/ directory.
File Processing:
Merges the cost file with the referral fee file based on Product Name.
Calculates the Total Cost for each product.
Outputs a new Excel file with the original data and the calculated Total Cost column.
Downloadable Output:
The processed file can be downloaded in .xlsx format.
Prerequisites
Python 3.x
Django
Pandas
OpenPyXL
How to Run
Step 1: Clone the Repository
git clone https://github.com/your-username/django-excel-app.git
cd django-excel-app

### Step 2: Install Dependencies

   -pip install -r requirements.txt

### Step 3: Set Up Django Project
   -python manage.py migrate
   -python manage.py runserver


### Step 4: Access the Application 
    Open your browser and navigate to these endpoints:
        ~ Upload Referral Fee File: http://127.0.0.1:8000/excelapp/referral-fee/
        
        ~ Process Cost File: http://127.0.0.1:8000/excelapp/process-cost-file/

 ### PROJECT STRUCTURE


products/
│
├── sales/
│   ├── templates/
│   │   ├── /upload.html
│   ├── views.py                   
│   ├── forms.py                   
│   ├── urls.py                   
│
├── media/                         
├── requirements.txt               
└── README.md                      




Frontend Functionality: User Data Page
The User Data page provides insights into the sales data, including total sales, product-specific sales, and a graphical representation. This page is implemented using HTML, JavaScript, and Chart.js and is integrated into the Django application.

Features
Total Sales Display:
Displays the total sales, calculated as the sum of the "Total Cost" column for all products.
Product-Specific Sales:
Each product has a button. Clicking the button shows the total sales for that specific product.
Graphical Representation:
Includes a bar chart showing the total sales for each product.
Steps to Use
Backend Endpoint:

The /user-data/ endpoint provides the sales data in JSON format:
total_sales: Total sales for all products.
product_sales: Dictionary of total sales for each product.
Frontend Page:

Access the User Data page at /user-data-page/.
