"""
Write a function most_prolific that takes a dict formatted like
Beatles_Discography example above and returns the year in which
the most albums were released.
If you call the function on the Beatles_Discography
it should return 1964, which saw more releases than
any other year in the discography.

If there are multiple years with the same maximum number of releases,
the function should return a list of years.
"""

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964,
    "Twist and Shout": 1964, "Help": 1965, "Rubber Soul": 1965,
    "Revolver": 1966, "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

def most_prolific(discography):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for album in discography:
        year = discography[album]
        if year in years:
            #if that year is already in the dictionary we raise its number
            years[year] += 1
        else:
            #if not we add it
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        #iterate on all years
        if years[year] > maxnumber:
            #if this year has more albums than previous
            #we consider this year to be the biggest
            maxyears = []
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            #if this year has the same number
            #but was not marked as a maximum before
            #we will mark it as a maximum
            maxyears.append(year)
    if (len(maxyears) == 1):
        # in the case of a single year with maximum number of albums
        # we return just that year
        return maxyears[0]
    else:
        # in case of multiple years with maximum albums
        # we return a list of them
        return maxyears



print(most_prolific(Beatles_Discography))
