# SPACE CODE PLATFORM

DJANGO MONGODB API

- Python >= 3.8

- Django 3.2.4

# Running application

## Step 1 - Install Python 3.8

```
sudo apt update
```

```
sudo apt install python3.8
```

- Once successfully installed, check your system Python versions

```
python --version
```

## Step 2 - Virtual Environment

- install pip3, the package manager for Python

```
apt-get install python3-pip
```

or

```
sudo pip3 install --upgrade pip
```

- Create:

```
pip3 install virtualenv
```

```
virtualenv galaxy
```

- Activate:

```
source galaxy/bin/activate
```

## Step 3 - Cloning application

- Clone

```
git clone https://github.com/MissHead/space-code-platform.git
```

- Go to project folder

```
cd space-code-platform/
```

- Installing dependencies

```
pip3 install -r requirements
```

## Step 4 - Setting up a MongoDB database container

```
cd mongodb/database/
```

```
sudo docker-compose up -d
```

```
cd ../../
```

```
python3 manage.py migrate
```

## Step 5 - Running

``` 
python3 manage.py runserver
```

- Test API health

```
curl http://127.0.0.1:8000/health
```

- Running tests

```
python3 manage.py test
```