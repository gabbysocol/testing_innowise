*** 

<br>   

#### Topic: 
A simple CRUD application for CRM system 

###### contents

* :earth_africa: __Adding companies__  

* :earth_africa: __Adding company stuff__   

* :earth_africa: __Filtration stuff by speciality__  

* :earth_africa: __Adding relationship between companies__  

***  

<br> 

#### To start:

 Clone the project  

    git clone https://github.com/gabbysocol/testing_innowise.git

    cd crm_project

 Create Python 3 virtual environment  

    virtualenv crm

 Activate the virtual environment  

    crm/Scripts/activate

 Install required packages  

    pip install -r requirements.txt

 Create database tables for the project  
    
    python manage.py migrate

 Run the development server

    python manage.py runserver
