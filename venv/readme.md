first i created a venv with the command: python -m venv venv(its the name of the env,,can be any name)

after that i activated the env : venv\Scripts\Activate 

now after getting into the venv i installed fastapi & uvicord(webserver to run fastapi apps) ,,, now i can see a lot of dependencies & libraries installed inside the Lib\site-packages folder...these are all the things needs to run the fastapi and uvicorn..

if i run this command : pip freeze > requirements.txt : so it will just list all the packages installed and write inside the requirments.txt file.

so why its imp ? lets say i wanna share this env with others ,,so how they gonna run and know what libraries used ? so if they just do pip install -r requirments.txt ,,the exact same env will be created to run the applicaition or model.


 