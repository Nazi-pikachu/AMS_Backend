# AMS_Backend

**Assignment for Alpha health**
_BASIC SETUP_

- First clone the repo
- RUN `pip install requirements.txt` to install all the dependecies
- RUN `py manage.py makemigrations`
- RUN `py manage.py migrate`

_TO RUN THE APP_

- -Make sure you are in the root directory i.e the same directory as **manage.py**
- -RUN `py manage.py runserver`

- [ ] NOTE:

> If running both the frontend and backend on the same machine then make
> sure to enable CORS **temporarily** to do so

- Go to the settings file in the AMS directory using `cd AMS`
- Add the address in the `CORS_ALLOWED_ORIGINS = [ 'http://localhost:3001',]`

### DataBase Diagram

    	ADMIN
    	DOCTOR(FK)<-------APPOINTMENT------------->(FK)PATIENT

#### API endpoints

_<a href = "https://github.com/Nazi-pikachu/AMS_Backend/blob/37693601f4120f3b957b0b4e194e4f68a3311373/AMS.pdf">API endpoints</a>_

#### Backend Architecture:

- Current application has a very simple monolith architecture which is
  built using django and djano-DRF.
- Additionally REST API are created to interact with the resources.

Possible use of cache/CDN/Load Balancers

CDN : If the application requires some large size images or other resources then CDN can be used for those purpose it will essentially help in

1.  **Improving website load times** - By distributing content closer to website visitors by using a nearby CDN server (among other optimizations), visitors experience faster page loading times. As visitors are more inclined to click away from a slow-loading site, a CDN can reduce bounce rates and increase the amount of time that people spend on the site. In other words, a faster a website means more visitors will stay and stick around longer.
2.  **Increasing content availability and redundancy** - Large amounts of traffic or hardware failures can interrupt normal website function. Thanks to their distributed nature, a CDN can handle more traffic and withstand hardware failure better than many origin servers.

Load balancers:
Significant large userbase will take a toll on the current monolith architecture , a better alternative in these cases would be to use a microservices architecture and a load balancer would be helpful in distributing the loads on the server.
