
# AMS_Backend
**Assignment for Alpha health**

*BASIC SETUP* 

 - First clone the repo
 - RUN `pip install requirements.txt` to install all the dependecies
 - RUN `py manage.py makemigrations`
 - RUN `py manage.py migrate`

*TO RUN THE APP*

 - -Make sure you are in the root directory i.e the same directory as **manage.py**
 - -RUN `py manage.py runserver`

### DataBase Diagram

		ADMIN
		DOCTOR(FK)<-------APPOINTMENT------------->(FK)PATIENT
		

#### API endpoints

*<a href = "https://github.com/Nazi-pikachu/AMS_Backend/blob/37693601f4120f3b957b0b4e194e4f68a3311373/AMS.pdf">API endpoints</a>*
