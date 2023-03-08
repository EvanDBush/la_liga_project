* Project: 
    
    Exploring Spanish Soccer League (la liga) data from 1929-2022. 
    
    
    Starting with an exploration of the data in 
    
    spain_explore.ipynb,
    
    I went on to look at each column in more detail in 
    
    spain_column_analysis.ipynb.

    After getting a better idea of the shape of the data, I came up with 
    questions that the data could answer. Some of these questions concerned
    data that didn't seem as useful or anamolous. 

    in the folder 
    
    /column_questions/ I attempt to answer these questions by columns.
    
    In

    spain_cleaning.ipynb, 
    
    I try and collect and answer questions that concerned 
    whether or not to use specific columns. In some cases, entire columns were created 
    to denote smoething different about a smaller set records. These cases were evaluated to
    be edited or deleted from the dataframe.

    spain_clean.py 

    is a script to run on the spain.csv file to create an edited datafrome in the results folder, labled: spain_clean.csv
    the command to run in the terminal for this file is:

    ```$ python spain_clean.py data/spain.csv results/spain_clean.csv```


    From this point on, I use spain_clean.csv as the spain_df in the following notebooks and scripts.


Goals: 

I  wanted to create a way to see the winners and standings for each season.
    
    - Calculate winning and losing totals by teams.
    - Calculate winning and losing streaks for Barcelona.
    - Use data to give teams points of wins, draws, and losses.
    - Use data to calculate Standings and Winners for each season.
    
    
And output data about a specific chosen team. Such as:
        - Total Wins, Draws, Losses
        - Longest Winning Streak/ Losing Streak
        - Win percentages home and away
        - Record Head-to-head with other teams (overall, last 5 meetings)





- Make a function that takes a season and team and returns their schedule and results
- Make a function that takes in a team and returns total wins, draws, and losses.

if I add data:

- Extend these methods to other leagues.
- Cross data with coaches for specific team. (Barcelona)
- Compare coaches winning percentages.

- Compare wins and losses pre-Messi, during Messi and post Messi.



Features:

(x) 1. Read in data from a local csv, excel file, json, or any other
file type. There are many ways to do this, but using
Pandas read_ functions is pretty easy.

On Line 1 of spain_explore.ipynb,

```
import pandas as pd

spain_df = pd.read_csv("data/spain.csv")
```
This same code is sucessfully used in every file of the project. If pandas is not working, please download the dependencies listed in requirements.txt


(x) 2. Use at least 5 different built-in Python functions to find out
something about your data. If you had a list for example,
finding the length of that list with len(<list>) does tell us a
little bit about the data.

() 3. Do 5 basic calculations with
Pandas, like finding the
sum(), median(), mean(), or
mode() of a column. You
could divide two columns by
each other. You could
multiple a column by a
random integer. You could
use string operations and find
the most common letter in a
given entry.

() 4. Make 2 basic plots with
matplotlib, seaborn, or any
other kind of visualization
library that you think looks
interesting.

(x) 5. Write markdown cells in
Jupyter explaining your
thought process and code. If
you make a few plots with
matplotlib, explain what the
reader is seeing and why you
chose to plot things that way.

Sources:

data - https://github.com/jalapic/engsoccerdata
gitignore - https://github.com/github/gitignore/blob/main/Python.gitignore