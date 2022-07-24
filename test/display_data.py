def display_data(df):
    # ask user if he want to see row data
    display = input('Would you like to see some of the row data? "yes" or "no"\n').lower()
    if display == 'yes':
        print(df.head(5))
        display = input('Would you like to see more of the row data? "yes" or "no"\n').lower()
        # check if he want to see more data
    while display == 'yes':
        for i in range(6,1000,5):
            print(df.loc[i-5:i, :]
            display = input('Would you like to see more of the row data? "yes" or "no"\n').lower()
            if display != 'yes':
               break
                  
view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
start_loc = 0
while (?????):
  print(df.iloc[????:????])
  start_loc += 5
  view_data = input("Do you wish to continue?: ").lower()