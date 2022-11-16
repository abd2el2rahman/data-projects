import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

month_list=['january','februaru','march','april','may','june','all']
weekday_list=['sunday','monday','tuesday','wdnesday','thursday','friday','saturday','all']

#function to validate user input
def check_user_input(user_input,input_type):
    while True:
        input_user_entered=input(user_input).lower()
        try:
            if input_user_entered in ['chicago', 'new york city' , 'washington'] and input_type == 'c':
                break
            elif input_user_entered in month_list and input_type == 'm':
                break
            elif input_user_entered in weekday_list and input_type == 'd':
                break
            else:
                if input_type == 'c':
                    print("invalid input!, input must be: chicago, new york city, or washington ")
                if input_type == 'm':
                    print("invalid input!, input must be: january, february, march, april, may, june or all")
                if input_type == 'd':    
                    print("invalid input!, input must be: sunday, monday, tuesday, wednesday, thursday, friday, saturday or all")
                    
        except ValueError:
                    print("input is wrong")
    return input_user_entered            

def get_filters():
   
   
    city = check_user_input("would you like to see the data for chicago, new york city or washington?\n",'c')

    month = check_user_input("plese enter month name from (january, february, march, april, may, june) otherwise enter 'all'\n",'m') 

    day = check_user_input("plese enter day name from (sunday, monday, tuesday, wednesday, thursday, friday, saturday) otherwise enter 'all'\n", 'd')

    print('*'*40)
    return city, month, day

def load_data(city, month, day):
    
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df                    
  

def time_stats(df):
   

    print('\ncalculating the most frequent times of travel...\n')
    start_time = time.time()

    #display the most common month
    m_c_m = df['month'].mode()[0]
    print('most common month is: ', m_c_m)

    #display the most common day of week
    m_c_d = df['day_of_week'].mode()[0]
    print('most common day is: ', m_c_d )

    #display the most common start hour
    m_c_h = df['hour'].mode()[0]
    print('most common start hour is: ', m_c_h)

    
    print('*'*40)
    


def station_stats(df):
  
    print('\ncalculating the most popular stations and trip...\n')
    start_time = time.time()

    m_c_s_s = df['Start Station'].mode()[0]
    m_c_e_s = df['End Station'].mode()[0]
    print('most common start station is: ', m_c_s_s)
    
    print('most common end station is: ', m_c_e_s)

    
    combination_group=df.groupby(['Start Station','End Station'])
    m_f_c_s = combination_group.size().sort_values(ascending=False).head(1)
    print('most frequent combination of start station and end station trip is: ', m_f_c_s)

   
    print('*'*40)

def trip_duration_stats(df):
   

    print('\ncalculating trip duration...\n')
    start_time = time.time()

    #display total travel time
    t_t_t = df['Trip Duration'].sum()
    print('total travel time is: ', t_t_t)


    #display mean travel time
    m_t_t= df['Trip Duration'].mean()
    print('mean travel time is: ', m_t_t)

   
    print('*'*40)


def user_stats(df,city):
   
    print('\ncalculating user stats...\n')
    start_time = time.time()

    #Display counts of user types
    print('user types in data are: ',df['User Type'].value_counts())
  

    if city != 'washington':
        
        print('counts Of gender: ',df['Gender'].value_counts())

        e_y = df['Birth Year'].min()
        print('earliest year is: ',e_y)

        m_r_y = df['Birth Year'].max()
        print('most recent year is: ',m_r_y)

        m_c_y = df['Birth Year'].mode()[0]
        print('most common year is: ',m_c_y)

        print('*'*40)
        
def main():
 
    while True:
        city,month,day = get_filters()      
        df = load_data(city,month,day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        restart = input('\nwont to restart? enter "y" for yes or "n" for no.\n').lower()
        if restart.lower() != 'y':
            break
        
if __name__ == "__main__":
	main()