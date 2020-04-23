import random

def best_car():
    #Prints a silly statement
    return "The Mitsubishi Lancer Evolution X, of course."

def wangan_course():
    '''Function to randomly generate a course to play for Wangan Midnight
    Maximum Tune 5 (NA)'''

    #lists with all courses and corresponding directions for certain courses
    courses = ['C1', 'Yaesu', 'New Belt Line', 'Wangan', 'Yokohane', 'Minato Mirai',
                'Nagoya Area', 'Osaka Area', 'Fukuoka Expressway', 'Hakone', 'Mt. Taikan']
    c1Directions = ['Inward', 'Outward']
    nblDirections = ['Clockwise', 'Counterclockwise']
    wanganDirections = ['Westbound', 'Eastbound']
    yokohaneDirections = ['Upward', 'Downward']
    dayTime = ['Morning','Night']

    finalCourse = ''
    chosenDirection = ''

    chosenCourse = random.choice(courses)
    chosenTime = random.choice(dayTime)
    #after choosing a course, chooses a proper direction for course
    if (chosenCourse in ['C1', 'Yaesu', 'Minato Mirai', 'Hakone']):
            chosenDirection = random.choice(c1Directions)
    elif (chosenCourse == 'New Belt Line'):
        chosenDirection = random.choice(nblDirections)
    elif (chosenCourse == 'Wangan'):
        chosenDirection = random.choice(wanganDirections)
    elif (chosenCourse == 'Yokohane' or chosenCourse == 'Mt. Taikan'):
        chosenDirection = random.choice(yokohaneDirections)

    #Deciding what to print based on course
    if chosenDirection != '':
        finalCourse = chosenCourse + ' ' + chosenDirection + ' ' + chosenTime
    else:
        finalCourse = chosenCourse + ' ' + chosenTime
    return finalCourse

def id8_course():
    '''Function to randomly generate a course to play in Initial D
    Arcade Stage 8: Infinity'''

    #list of all courses and directions
    courses = ['Lake Akina', 'Usui', 'Myogi', 'Akagi', 'Akina', 'Irohazaka', 'Hakone',
               'Tsukuba', 'Sadamine', 'Tsuchisaka', 'Momiji Line', 'Happogahara', 'Nanamagari',
               'Nagao', 'Tsubaki Line', 'Akina (Snow)']
    defaultDirections = ['Downhill', 'Uphill']
    usuiDirections = ['Clockwise', 'Counterclockwise']
    tsukubaDirections = ['Outbound', 'Inbound']
    dayTime = ['Day', 'Night']

    #Deciding course and corresponding directions
    finalCourse = ''
    chosenDirection = ''
    chosenTime = ''

    chosenCourse = random.choice(courses)
    if chosenCourse == 'Lake Akina' or chosenCourse == 'Usui':
        chosenDirection = random.choice(usuiDirections)
    elif chosenCourse in ['Tsukuba', 'Tsuchisaka', 'Happogahara']:
        chosenDirection = random.choice(tsukubaDirections)
    else:
        chosenDirection = random.choice(defaultDirections)

    if not chosenCourse == 'Akina (Snow)':
        chosenTime = random.choice(dayTime)

    finalCourse = chosenCourse + ' ' + chosenDirection + ' ' + chosenTime
    return finalCourse
