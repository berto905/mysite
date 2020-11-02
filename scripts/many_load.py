import csv

# https://docs.python.org/3/library/csv.html
# https://django-extensions.readthedocs.io/en/latest/runscript.html
# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)    # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude, area_hectares
    # category, states, region, iso

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(category=row[7])
        st, created = States.objects.get_or_create(states=row[8])
        rg, created = Region.objects.get_or_create(region=row[9])
        iso_, created = Iso.objects.get_or_create(iso=row[10])

        try:
            yr = int(row[3])
        except:
            yr = None

        try:
            lon = float(row[4])
        except:
            lon = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            ah = float(row[6])
        except:
            ah = None

        site = Site(name=row[0], description=row[1], justification=row[2],
                    year=yr, longitude=lon, latitude=lat, area_hectares=ah,
                    category=cat, states=st, region=rg, iso=iso_)
        site.save()



# Original script

# from many.models import Person, Course, Membership

# def run():
#     fhand = open('many/load.csv')
#     reader = csv.reader(fhand)
#     next(reader)    # Advance past the header

#     Person.objects.all().delete()
#     Course.objects.all().delete()
#     Membership.objects.all().delete()

#     # Format
#     # email,role,course
#     # jane@tsugi.org,I,Python
#     # ed@tsugi.org,L,Python

#     for row in reader:
#         print(row)

#         p, created = Person.objects.get_or_create(email=row[0])
#         c, created = Course.objects.get_or_create(title=row[2])

#         r = Membership.LEARNER
#         if row[1] == 'I':
#             r = Membership.INSTRUCTOR
#         m = Membership(role=r, person=p, course=c)
#         m.save()