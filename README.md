[![Build Status](https://travis-ci.org/Philipotieno/FAST_FOOD_FAST.svg?branch=ch-tests)](https://travis-ci.org/Philipotieno/FAST_FOOD_FAST) [![Coverage Status](https://coveralls.io/repos/github/Philipotieno/FAST_FOOD_FAST/badge.svg?branch=ch-tests)](https://coveralls.io/github/Philipotieno/FAST_FOOD_FAST?branch=ch-tests)

## Fast-Food-Fast
Fast-Food-Fast is a food delivery service app for a restaurant

## Features
- Users can create an account.
- Signed up users can log into their account.
- Users can post orders.
- Users can get history of orders.
- Users can get a specific order.
- Users can modify an order.

## Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python microframework)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)


## Getting Started:

**You can view the app on heroku at [https://chiemo.herokuapp.com/](https://chiemo.herokuapp.com/) and test the end points on postman

or


**To Test the followig endpoints with postman:**

| Method   |Description            |Endpoint                            |
| ---------|-----------------------|------------------------------------|
| POST     |Register users         |/api/v1/users/signup                |
| POST     |Log in users           |/api/v1/users/login                 |
| POST     |Make an order          |/api/v1/users/orders                |    
| GET      |Get all orders         |/api/v1/users/orders                |   
| GET      |Get specific orders    |/api/v1/users/orders/<int:order_id> |   
| PUT      |Update specific orders |/api/v1/users/orders/<int:order_id> |   

**To start the following app, follow the instructions below:**

**On your terminal:**

Install pip:

  $ sudo apt-get install python-pip

Clone this repository:

  $ git clone https://github.com/Philipotieno/FAST_FOOD_FAST.git

Get into the root directory:

  $ cd FAST_FOOD_FAST/

Install virtualenv:

  $ pip install virtualenv

Create a virtual environment in the root directory:

  $ virtualenv -name of virtualenv-
  
 Note: If you do not have python3 installed globally, please run this command when creating a virtual environment:
 
   $ virtualenv -p python3 -name of virtualenv-

Activate the virtualenv:

  $ source name of virtualenv/bin/activate

Install the requirements of the project:

  $ pip install -r requirements.txt

Run the application:

  $ python run.py

To run tests:

  $ pytest