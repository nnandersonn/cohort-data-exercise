"""Functions to parse a file containing student data."""


from enum import unique
from matplotlib.pyplot import cohere


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()
    data = open(filename)
    for line in data:
      first, last, house, adviser, cohort = line.split('|')
      if house != '':
        houses.add(house)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    data = open(filename)
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')

      if cohort_raw != "I" and cohort_raw != "G":
        if cohort == "All":
          students.append(f"{first} {last}")
        elif cohort_raw == cohort:
          students.append(f"{first} {last}")
    
      

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    data = open(filename)
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')
    
      if cohort_raw == "I":
        instructors.append(f"{first} {last}")
      elif cohort_raw == "G":
        ghosts.append(f"{first} {last}")
      elif house == "Dumbledore's Army":
        dumbledores_army.append(f"{first} {last}")
      elif house == "Gryffindor":
        gryffindor.append(f"{first} {last}")
      elif house == "Hufflepuff":
        hufflepuff.append(f"{first} {last}")
      elif house == "Ravenclaw":
        ravenclaw.append(f"{first} {last}")
      elif house == "Slytherin":
        slytherin.append(f"{first} {last}")



    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    data = open(filename)
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')
      all_data.append((f"{first} {last}", house, adviser, cohort_raw))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    data = open(filename)
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')
      try: 
        input_first, input_last = name.split()
        if input_first == first and input_last == last:
          return cohort_raw
          break
      except:
        return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    unique_last = set()
    dup_last = []
    data = open(filename)
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')
      if last in unique_last and last not in dup_last:
        dup_last.append(last)
      else:
        unique_last.add(last)
    return dup_last


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    data = open(filename)
    input_first, input_last = name.split()
    student = []
    housemates = set()
    
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')
      if first == input_first and last == input_last: 
        student.append(first)
        student.append(last)
        student.append(house)
        student.append(cohort_raw)
        break
    data.seek(0)
    for line in data:
      first, last, house, adviser, cohort_raw = line.rstrip().split('|')
      if house == student[2] and cohort_raw == student[3] and first != student[0] and last != student[1]:
        housemates.add(f"{first} {last}")

    return housemates


     
    



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
