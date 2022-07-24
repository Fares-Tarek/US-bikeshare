
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types: \n ", user_types, "\n")
    # TO DO: Display counts of gender
    try:
        print("gender count : {}".format(df['gender'].value_counts()))
    except:
          print("gender not available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()[0]
        recent_birth = df['Birth Year'].max()[0]
        common_year = df['Birth Year'].mode()[0]
        print("Earliest year of birth is: {}\n Most recent year of birth is: {}\n Most common year of birth is: {}\n".format(earliest_birth, recent_birth, common_year))
    except:
           print("Birth year not available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)