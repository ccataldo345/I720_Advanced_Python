DESCRIPTION
------------

Python project for I720 Advanced Python course.

Write a script that takes the following json data (https://blockchain.info/charts/market-price) and can tell the user the following information:

What is the highest price in the the data, and what day was it?
What was the greatest percent increase over the previous day, and what day was it?
What was the greatest percent decrease over the previous day, and what day was it?



USAGE
-----

`project.py`


UNIT TEST
-----
`python3 -m unittest test_main.py`

(check if the last date of the values in the list corresponds to the date of yesterday)

REQUIREMENTS
-----

requests==2.9.1
