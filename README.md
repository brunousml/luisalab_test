# Test Luisa_labs

# Create a virtual environment
Follows this link to create your virtualenv
https://virtualenv.pypa.io/en/latest/userguide/

## Start Server
This command will install dependencies with pip. After install dependencies he will run command
runserver.

PS: Check requirements.txt file to ensures all libs are installed. For example
 mysql libs and xml libs to your operational system.

```make start```

## Test api
This command will run a request to api ```curl -H "Content-Type: application/javascript" http://localhost:8000/employee/```

```make test.api.get.employee```