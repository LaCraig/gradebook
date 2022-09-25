import pandas as pd
names = ['m','p','r','a','l']
subjects = ['ma', 'sp', 'gr', 'ge', 'fm', 'cs', 'sc', 'li', 'co', 'hi', 'ti', 're']
assignments = ['t', 'q', 'd']
def main():
    gradebook = pd.DataFrame(columns= ['Name', 'Grade', 'Subject', 'Type', 'Date'])
    entry = input('At anytime you can type exit to close. \n'
                'Enter Name, Grade, Subject, Assignment, Date\n'
                'example: m 95 sc q 12/03/22:  ').lower().split(' ')
    if 'exit' in entry:
        import sys
        sys.exit()
    if len(entry) != 5:
        print('Wrong number of arguments. Only accepts 5. Try again')
        main()

    name = name_check(entry[0])
    grade = grade_check(entry[1])
    subject = subject_check(entry[2])
    assignment = assignment_check(entry[3])
    date = date_check(entry[4])

    gradebook = gradebook.append({
        'Name' : name,
        'Grade' : grade,
        'Subject' : subject,
        'Type' : assignment,
        'Date' : date
        }, ignore_index=True)

    gradebook.to_csv('grade_database.csv', mode='a', index=False, header=False)

def name_check(name):
    if name not in names:
        print(f'That is not an acceptable entry. Your options are: \n{names}')
        main()
    elif name == 'm':
        return 'Mychaela'
    elif name == 'p':
        return 'Paxton'
    elif name == 'r':
        return 'Regina'
    elif name == 'a':
        return 'Adelaide'
    elif name == 'l':
        return 'Luciana'
    
def grade_check(grade):   
    try:
        return int(grade)
    except ValueError:
        print('You did not enter a number. Try again.')
        main()

def subject_check(subject):
    if subject not in subjects:
        print(f'You did not enter an appropriate subject. Your options are:\n{subjects}')
        main()
    elif subject == 'ma':
        return 'Math'
    elif subject == 'sp':
        return 'Spelling'
    elif subject == 'gr':
        return 'Grammar'
    elif subject == 'ge':
        return 'Geography'
    elif subject == 'fm':
        return 'FMMA'
    elif subject == 'cs':
        return 'CS'
    elif subject == 'sc':
        return 'Science'
    elif subject == 'li':
        return 'Literature'
    elif subject == 'co':
        return 'Composition'
    elif subject == 'hi':
        return 'History'
    elif subject == 'ti':
        return 'Timeline'
    elif subject == 're':
        return 'Religion'

def assignment_check(assignment):
    if assignment not in assignments:
        print(f'That is not an acceptable assignment choice. Your options are: \n{assignments}')
        main()
    elif assignment == 't':
        return 'Test'
    elif assignment == 'q':
        return 'Quiz'
    elif assignment == 'd':
        return 'Daily'

def date_check(date):
    try:
        return pd.to_datetime(date)
    except:
        'You did not type an acceptable date format. Try: mm/dd/yy'
        main()

main()

# def main():
#     entry = input('Who do you wish to ')
#     grades()

# def grades(name, subject, grade, date):
#     name = name.capitalize()
#     grade = grade/100

