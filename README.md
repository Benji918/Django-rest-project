# Zenrapy Django RESTFUL API 
Backend user authentication for registration and login

Django Rest Framework Documentation ](https://www.django-rest-framework.org/)


### How to setup locally
#### Requirements

- Python3.7
- pip3
- virtualenv


#### setup instructions

- pull the project using git
```cmd
   git clone https://github.com/Zenrapy-V1/zenrapy-backend.git
   ```
- create   a virtualenv using virtualenv
```cmd
   python -m pip install --upgrade pip
   pip install virtualenv
   virtualenv venv_name
   ```
- activate it 
```cmd
   source venv_name/bin/activate
   ```
- or activate Windows
```cmd
   venv_name/bin/activate.bat
   ```
- install dependencies from the requirements.txt file
```cmd
   pip install -r requirements.txt
   ```
- create a MongoDb database and establish a connection
#### Make sure the database name is the same with the one in the settings.py file to prevent errors
#### Collection name is irrelevant
![](images\zenrapydb.jpg "MongoDB database")

- migrate the database tables
```cmd
   python manage.py migrate
   ```
- start a development server using 
```cmd
   python manage.py runserver
   ```
### How to run model tests
#### Requirements

- First install coverage
```cmd
   pip install coverage
```
- Next, in the terminal run the command
```cmd
    coverage run manage.py test && coverage report && coverage html
```
- cd into the htmlcov folder, open the index.html file to see the tests being run


### How to use swagger
#### Requirements

- First install coverage
```cmd
   pip install drf-yasg
```
- Then in the url tab
```cmd
    http://127.0.0.1:8000/swagger/
```
- This is what you should see
![](https://github.com/Zenrapy-V1/zenrapy-backend/blob/Benji/images/testing api.jpg)

- To add the API documentation to Postman
```cmd
    http://127.0.0.1:8000/swagger.json/
```
- A json file will be downloaded, then go to Postman
- Follow the instructions in the image
- Click on the 3 dashed lines
- Click on file
- Then click import
![](https://github.com/Zenrapy-V1/zenrapy-backend/blob/Benji/images/img.png)

- Click on the upload button
- Then select the json file
- Then click import
![](https://github.com/Zenrapy-V1/zenrapy-backend/blob/Benji/images/img_1.png)
