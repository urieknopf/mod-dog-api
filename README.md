# mod-dog-api
A Dockerized Django app with a PostgreSQL database and DjangoRestAPI

Welcome to the mod dog api where we have dogs and keys and keys and dogs!
(Disclaimer: Dogs currently pending. No dogs were harmed in the making of this application)

## To set up a local enviroment of the application, please remain in the ride at all times and do the following:

### Step 1: Acquire code
Clone the repository to your local machine [more information at this tutorial](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

### Step 2: Get your docker on
Make sure that docker works on your machine [more info about docker here](https://docs.docker.com/)
Open your terminal and navigate to the folder of the repository (the folder contains a folder named 'app', a docker-compose.yml file, a DockerFile file, and more)
Run the following command: 
> docker-compose build 

And run this command: 
> docker-compose up -d

(if the above commands give you issues, try running them with "docker compose", with a space instead of hyphen)
(there are a few ways to accomplish the past few steps, so if you have experience with docker and feel comfortable building and running the containers another way, go for it!)

### Step 3: Let's DjanGO
- open http://localhost:8000/ in your browser. It should say "Index loaded successfully"

## Step 4: There are two ways to access the API Endpoints, the terminal and curling is more exhaustive and the browser is simpler:

#### To access the API Endpoints via terminal:
To create a new key:
> curl -X POST http://localhost:8000/keys/

To Update an existing key:
> curl -X PUT http://localhost:8000/keys/<pk>/

To view all keys:
> curl -X GET http://localhost:8000/keys/

To view a specific key:
> curl -X GET http://localhost:8000/keys/<pk>/

#### To access the API Endpoints via browser:
To view all keys:
> http://localhost:8000/keys/

To view a specific key:
> http://localhost:8000/keys/<pk>/
(where <pk> is replaced with primary key or id of key)

## Other things to do:
### Run Tests:
exec into the docker container by running the following command (more documentation here: https://docs.docker.com/engine/reference/commandline/exec/):
> docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
You can find the container name by running docker ps and looking for the container you want to exec into. 
For example, when run on my local machine running ubuntu the command is:
> docker exec -it mod-dog-api_app_1 /bin/sh
But this may be just "bash" instead of /bin/sh on certain machines.
Once in the container (the terminal prompt should have changed to something like "/app $") run:
> python manage.py test
