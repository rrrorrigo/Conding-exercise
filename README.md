# Coding exercise

### Overview Solution
The exercise is about creating a script that is able to, given a txt file as input, with the format of:
NAME=MO12:00-14:00
where MO is a reference to the first two letters of Monday and the hours worked separated by a hyphen.

Seeing this, I decided to change the strings to numbers, for a better handling of the data, since later it would be necessary to make comparisons with them. All this procedure for each worked day put as input

### Architecture
I opted to separate the function from the main file, mostly for better organization. The execution should be done to the main.py file.

### Methodology
As I mentioned before, I opted to exchange strings for numbers for better handling. This was done manually with the days of the week, hours and hourly payments.

After the creation of these variables everything was much easier, it was only necessary to separate the data from the integer string and then do a multiplication of the hour in which it started to work with the amount of hours worked.

### Instructions
The execution is quite intuitive, after being executed the main file will ask you to enter the path to the txt file. I did some simple error handling like making a mistake with the file name or that the format of the hours worked are wrongly set.

Example of execution:
```
    python .\main.py
```
