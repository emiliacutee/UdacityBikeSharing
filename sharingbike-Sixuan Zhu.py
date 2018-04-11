#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:54:51 2018

@author: Sixuan Zhu
"""
import time
import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt


CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Of which city would you like to see the data? (Chicago, NYC or Washington?)\n').lower()
        if city in ('chicago', 'nyc', 'washington'):
            break
        else:
            print('invalid input, please try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    #choose filter
    while True:
        filters = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter\n").lower()
        if filters in ('month','day','both','none'):
            break
        else:
            print('invalid input, please try again')


    if filters == 'month':
        day = 'all'
        while True:
            month = int(input("Which month(month 1-6 data avaliable)? Please type your response as an integer (e.g 1 for January)\n"))
            if month in np.arange(1,7):
                break
            else:
                print('invalid input, please try again')

    elif filters == 'day':
        month = 'all'
        while True:
            day = int(input("which day of week? Please type your response as an integer(0-6) (e.g 0 for monday, 6 for sunday)\n"))
            if day in np.arange(0,8):
                break
            else:
                print('invalid input, please try again')

    elif filters == 'both':
        while True:
            day = int(input("which day of week? Please type your response as an integer(0-6) (e.g 0 for monday, 6 for sunday)\n"))
            if day in np.arange(0,8):
                break
            else:
                print('invalid input, please try again')

        while True:
            month = int(input("Which month(month 1-6 data avaliable)? Please type your response as an integer (e.g 1 for January)\n"))
            if month in np.arange(1,7):
                break
            else:
                print('invalid input, please try again')

    else:
        month = 'all'
        day = 'all'

    print('-'*40)
    return city, str(month), str(day)


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'],format='%Y-%m-%d %H:%M:%S')
    df['End Time'] = pd.to_datetime(df['End Time'],format='%Y-%m-%d %H:%M:%S')
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    #when filter is 'both':
    if (month != 'all') and (day != 'all'):
        df = df[(df['month']==int(month)) & (df['day_of_week'] == int(day))]

    #when filter is 'day':
    elif (day != 'all') and (month == 'all'):
        df = df[df['day_of_week'] == int(day)]

    #when filter is 'month':
    elif (month != 'all') and (day == 'all'):
        df = df[df['month'] == int(month)]

    #when filter is 'none':
    else:
        df = df

    return df



def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    pop_month_name = calendar.month_name[pop_month]
    # TO DO: display the most common day of week
    pop_weekday = df['day_of_week'].mode()[0]
    pop_weekday_name = calendar.day_name[pop_weekday]
    # TO DO: display the most common start hour
    pop_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    month_result = '\nIn the month of {} people travel most.\n'.format(pop_month_name)
    weekday_result = '\nOn {} people travel most.\n'.format(pop_weekday_name)
    hour_result = '\nBetween {}:00 and {}:00 people travel most.\n'.format(pop_hour, pop_hour+1)

    #filter = month
    if (month != 'all') and (day == 'all'):
        print ('\nIn the month of {},\n'.format(calendar.month_name[int(month)]), weekday_result, hour_result)
    #filter = day
    elif (day != 'all') and (month == 'all'):
        print ('\nOn {}s,'.format(calendar.day_name[int(day)]), month_result, hour_result)
    #filter = both
    elif (day != 'all') and (month != 'all'):
        print ('\nOn {}s in every {} of a year,'.format(calendar.day_name[int(day)],calendar.month_name[int(month)]),hour_result)
    #filter = none
    elif (day == 'all') and (month == 'all'):
        print (month_result, weekday_result, hour_result)
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    pop_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = 'from station ' + df['Start Station'] + ' to station ' + df['End Station']
    pop_trip = df['Trip'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print ('\nThe most popular start station is {};\nThe most popular end station is {};\nThe most popular trip is {}.\n'.format(pop_start, pop_end, pop_trip))
    print ('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['Trip Duration'] = df['End Time'] - df['Start Time']
    # TO DO: display mean travel time
    trip_duration_mean = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print ('\nThe average trip takes {}.\n'.format(trip_duration_mean))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # TO DO: Display counts of user types
    print('\nAnalysing User Type info...\n')
    user_types = df['User Type'].value_counts()
    #plot bar chart for user type
    print('plotting user type info:')
    axes = user_types.plot(kind='bar', title ="Distribution of User type", rot= 0)
    axes.set_xlabel('User types')
    axes.set_ylabel('Frequency')

    #annotate bars with its percentage
    totals = []
    for i in axes.patches:
        totals.append(i.get_height())
        total = sum(totals)
    
    for i in axes.patches:
        axes.text(i.get_x()+.07, i.get_height()+1000, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=12, color ='black')
    plt.show()

    # TO DO: Display counts of gender
    if city == 'washington':
        print ('\nUser type info for city {}:\n'.format(city))
        print (user_types)
        print('\nNo gender or user birth year info avaliable for Washington.\n')
        print('-'*40)

    else:
        #print user type info
        print ('User type info for city {}:\n'.format(city))
        print (user_types)
        
        #Analysing gender info
        print('\nAnalysing gender info of city {}:\n'.format(city))
        gender = df['Gender'].value_counts()
        print (gender)
        
        #plot bar chart for gender
        print('\nPlotting gender info of city {}\n:'.format(city))
        axes = gender.plot(kind='bar', title ="Distribution of Gender", rot= 0)
        axes.set_xlabel('Gender')
        axes.set_ylabel('Frequency')

        #annotate bars with its percentage
        totals = []
        for i in axes.patches:
            totals.append(i.get_height())
            total = sum(totals)
    
        for i in axes.patches:
            axes.text(i.get_x()+.1, i.get_height()+1000, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=12, color ='black')
        
        plt.show()
        
        
        
        
        #Analysing birth year info
        print('\nAnalysing users\' birth year info of city {}:\n'.format(city))
        
        birth_year = df['Birth Year']
        birth_year = birth_year.dropna().astype(int)
        #Here we assume that people over 80 or under 10 cannot ride bikes. 
        #Therefore birth_year > 80 or <10 will be taken as invalid inputs.
        p1 = (2017 - birth_year) <= 80
        p2 = (2017 - birth_year) >= 10
        birth_year = birth_year[p1 & p2]

        youngest = birth_year.max()
        oldest = birth_year.min()
        mode_birth = birth_year.mode()[0]

        print('\nIn general, the youngest user borned at {}.\nThe oldest user borned at {}.\nMost users borned at {}.\n'.format(youngest, oldest, mode_birth ))

        #ploting the distribution(histogram) of birth_year
        print('Plotting users\' birth year info of city {}'.format(city))
        ax = birth_year.hist(bins = 20, histtype='bar', ec='orange')
        ax.set_ylabel('Frequency')
        ax.set_xlabel('Users\' birth year')
        ax.set_title ("Distribution of users' birth year")
        plt.show()
        
        
        #Calulating the skewness of birth_year
        birth_skewness = birth_year.skew()
        
        if abs(birth_skewness) > 1:
            skew_deg = 'highly'
        elif 0.5 <= abs(birth_skewness) <= 1:
            skew_deg = 'moderately'
        elif abs(birth_skewness) < 0.5:
            skew_deg = 'approximately symmetric'

        if birth_skewness < 0:
            print ('\nUsers\' birth year is negatively skewed (degree = {}).\n'.format(skew_deg))
        elif birth_skewness > 0:
            print ('\nUsers\' birth year is positively skewed (degree = {}).\n'.format(skew_deg))
        else:
            print ('\nUsers\' birth year is normally distributed.\n')
        
        print('-'*15, 'This is the end of the analysis','-'*15)



def main():
    while True:
        plt.style.use('ggplot')
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
