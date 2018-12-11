from application.model.venue.location import Address
from application.model.venue.rating import Rating
from application.model.venue.utility.defaults import VenueDefaults


class Venue:

    def __init__(self, venue_id, venue_name, address, rating_review, other_info, licences, description, venue_type,
                 admin):

        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_type = venue_type
        self.rating = Rating(score=rating_review[0], review=rating_review[1])
        self.other_info = other_info
        self.description = description
        self.licences = licences
        self.admin = admin
        self.address = Address(line_1=address[0], line_2=address[1],
                               line_3=address[2], line_4=address[3], postcode=address[4])


class SportsCentre(Venue):

    def __init__(self, venue_id, venue_name, address):

        Venue.__init__(self, venue_id=venue_id, venue_name=venue_name,
                       venue_type=VenueDefaults.TYPE_SPORTS, address=address)


class AcademicInstitution(Venue):

    def __init__(self, venue_id, venue_name, address):

        Venue.__init__(self, venue_id=venue_id, venue_name=venue_name,
                       venue_type=VenueDefaults.TYPE_ACADEMIC, address=address)


class ReligiousPlace(Venue):

    def __init__(self, venue_id, venue_name, address):

        Venue.__init__(self, venue_id=venue_id, venue_name=venue_name,
                       venue_type=VenueDefaults.TYPE_RELIGIOUS, address=address)
