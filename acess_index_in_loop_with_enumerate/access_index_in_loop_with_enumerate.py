"""
HighFiveCode - https://highfivecode.com/
HFC YouTube Channel: https://www.youtube.com/channel/UCOmiui0ghT5OoVdD1wi4mFA
Send requests to: https://highfivecode.com/suggestions/
Python3 Built in functions: https://docs.python.org/3/library/functions.html

enumerate(iterable) takes an iterable and returns tuples of (index, iterable element)
optionally takes a second argument, "start" which tells the "index" where to start counting
"start" defaults to 0
"""

def main():
    countries = [
                    'colombia',
                    'brazil',
                    'peru',
                    'thailand',
                    'cambodia',
                    'vietnam'
                ]
    print('here is our list of countries Jon wants to visit.')
    print(countries)
    print('that display is ugly, lets loop over and create an indexed list')
    msg = 'You can do it using a \'count\' variable'
    msg += 'instead of built in functions:'
    print(msg)
    # use the "accumulator" method
    count = 0
    for country in countries:
        print("{}. {}".format(count, country))
        count += 1 # don't forget to increment count

    print('or you can use the built-in enumerate function:')
    # it returns a tuple of (index, element) for each iteration
    for tuple_index, tuple_elem in enumerate(countries):
        print("{}. {}".format(tuple_index, tuple_elem))

    msg = 'you can pass a second argument to enumerate to tell it'
    msg += 'where to start counting!'
    print(msg)
    # it returns a tuple of (index, element) for each iteration
    for tuple_index, tuple_elem in enumerate(countries, 53):
        print("{}. {}".format(tuple_index, tuple_elem))

if __name__ == "__main__":
    """
    Not sure what 'if __name__ == __main__' does?
    Check it out here: https://www.youtube.com/watch?v=5edEA2YYjLk
    """
    main()
