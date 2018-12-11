from application.model.venue.location import Address
from application.model.venue.venue import Venue


class Person:

    def __init__(self, person_id, first_name, last_name, address, mobile_number, email):

        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = Address(line_1=address[0], line_2=address[1],
                               line_3=address[2], line_4=address[3], postcode=address[4])

        self.mobile_number = mobile_number
        self.email = email

    def get_name(self):
        return self.first_name + " " + self.last_name


class AthleteUser(Person):

    def __init__(self, person_id, first_name, last_name, address, mobile_number, email, username, password):

        Person.__init__(self, person_id=person_id, first_name=first_name, last_name=last_name,
                        address=address, mobile_number=mobile_number, email=email)

        self.username = username
        self.password = password


class VenueAdmin(Person):

    def __init__(self, person_id, first_name, last_name, address, mobile_number, email, username, password,
                 associated_venue, authorisation_pin):
        Person.__init__(self, person_id=person_id, first_name=first_name, last_name=last_name,
                        address=address, mobile_number=mobile_number, email=email)

        self.username = username
        self.password = password
        self.authorisation_pin = authorisation_pin
        self.associated_venue = associated_venue
