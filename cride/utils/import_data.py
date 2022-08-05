import csv
import os

from cride.circles.models import Circle


def import_csv(csv_filename):
    my_file = os.path.join(os.getcwd(), csv_filename)
    with open(my_file, 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            circle, created = Circle.objects.get_or_create(**row)
            if not created:
                circle.save()
            print(circle.name)

    Circle.objects.filter(members_limit__gt=0).update(is_limited=True)

