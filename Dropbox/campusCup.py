# Dropbox holds a competition between schools called CampusCup. If you verify an email
# address from a college, university, or higher education institution, you earn 20 points
# toward your school's overall ranking. When a school receives at least 100 points,
# all of its registered members receive an additional 3 Gb of bonus space each.
# When the school receives at least 200 points, its registered members receive an
# additional 8 Gb. If the school receives at least 300 points, its members receive
# an additional 15 Gb. And finally, when a school receives at least 500 points,
# members receive an additional 25 Gb each.
#
# You are given n registered emails, all of them unique. Each email has the following
# format: "<name>@<domain>", where <name> and <domain> are non-empty strings consisting
# of lowercase letters and a '.'. Identical domains correspond to the same school and vice versa.
#
# Your task is to make a scoreboard, i.e. to sort the schools according to the amount
# of bonus space they each received (per student not in total). School A must be higher
# in the standings than school B if A received more space than B, or if they received
# equal number of gigabytes but the domain string of school A is lexicographically
# smaller than the one of school B.


def campusCup(emails):
    schools = dict()
    for email in emails:
        name, school = email.split("@")
        if school not in schools.keys():
            schools[school] = 20
        else:
            schools[school] += 20

    school_points = {
        0: [],
        100: [],
        200: [],
        300: [],
        500: []
    }

    for school, point in schools.items():
        if point >= 500:
            school_points[500].append(school)
        elif 300 <= point < 500:
            school_points[300].append(school)
        elif 200 <= point < 300:
            school_points[200].append(school)
        elif 100 <= point < 200:
            school_points[100].append(school)
        else:
            school_points[0].append(school)

    school_rank = list()

    if len(school_points[500]) > 0:
        school_points[500].sort()
        extend(school_rank, school_points[500])
    if len(school_points[300]) > 0:
        school_points[300].sort()
        extend(school_rank, school_points[300])
    if len(school_points[200]) > 0:
        school_points[200].sort()
        extend(school_rank, school_points[200])
    if len(school_points[100]) > 0:
        school_points[100].sort()
        extend(school_rank, school_points[100])
    if len(school_points[0]) > 0:
        school_points[0]
        extend(school_rank, school_points[0])

    return school_rank


def extend(lst1, lst2):
    for i in lst2:
        lst1.append(i)
