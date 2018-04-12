# UdacityBikeSharing
Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year
New York City sample bike share data
Data for the first 10 rides in the new_york_city.csv file

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!

The Questions
You will write code to answer the following questions about the bike share data:

What month occurs most often in the start time?
What day of the week (Monday, Tuesday, etc.) occurs most often in the start time? Hint: datetime.weekday() (documentation here) may be helpful!
What hour of the day occurs most often in the start time?
What is the total trip duration and average trip duration?
What is the most frequently used start station and most frequently used end station?
What is the most common trip (i.e., the combination of start station and end station that occurs the most often)?
What are the counts of each user type?
What are the counts of gender?
What is the earliest birth year (when the oldest person was born), most recent birth year, and most common birth year?
The Files
To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a bikeshare.py file, and you will do your scripting in there also. You will need the three city dataset files too:

chicago.csv
new_york_city.csv
washington.csv
All four of these files are zipped up in the Bikeshare file in the resource tab in the sidebar on the left side of this page, and you should download that zip file.

Once you have downloaded this zip file, move to the next page for more details on the code you will be writing.
