Flask Template Application
=============================

This is a template Flask application that can be used to quickly bootstrap a new Flask application.

The project is laid out according to the Flask and pytest best practices.

It includes a GitHub Actions workflow that lints and tests your code. This action can be easily configured to deploy to a CapRover instance (see [Deploy](#deploy)).

## Features

## Usage

### Local Development

Clone the repository:
```shell
git clone https://github.com/aaryan-dharmadhikari/flask-template
cd flask-template
```

Requires Python 3.8 or higher and `virtualenv` to be installed.

Setup virtual environment:
```shell
python -m venv .venv
source .venv/bin/activate
```
Make sure to activate the virtual environment every time you open a new terminal.

Install dependencies:
```shell
pip install -r requirements.txt
```

Run the application:
```shell
python -m flask --app src/myapp run --debug
```
View the application at http://localhost:5000.

Flask automatically reloads the application when changes are made.
Press `Ctrl+C` to stop running debug mode.

### Docker

Requires Docker engine to be installed.

Build image:
```shell
docker build --tag flask-template-docker .
```
This must be done between changes to the source code.

Run container:
```shell
docker run -p 5000:80 --name myapp flask-template-docker
```
View the application at http://localhost:5000.

Press `Ctrl+C` to stop the container. The `-d` flag can be added to the above command to run the container in the background.

Note: The docker image is configured to run the application on port 80 inside the container.


## Testing

Install test dependencies:
```shell
pip install .[test]
```

Run tests:
```shell
pytest
```

## GitHub Actions

### Linting

The `Lint` action runs `flake8` to check for linting errors.

### Testing

The `Test` action runs `pytest` to run unit tests.

### Deployment

The `Deploy App to CapRover` action packs the application into a tarball and uploads it to CapRover.

For this action to work, the following secrets must be set in the repository:
- `CAPROVER_SERVER`: the URL of the CapRover server.
- `APP_NAME`: the name of the application on CapRover.
- `APP_TOKEN`: the CapRover application token (found under Deployment).

See the [CapRover docs](https://caprover.com/docs/ci-cd-integration/deploy-from-github.html#deploying-directly-from-github) for more information.
