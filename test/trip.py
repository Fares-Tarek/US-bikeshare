def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()[0]
    print("Total travel time is: {}\n".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()[0]
    print("Average travel time is: {}\n".format(mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)