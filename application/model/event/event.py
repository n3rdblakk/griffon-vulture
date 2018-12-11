from application.model.venue.venue import Venue


class Event:

    def __init__(self, event_id, event_name, venue, max_capacity, participants, room, organiser):

        self.event_id = event_id
        self.event_name = event_name
        self.max_capacity = max_capacity
        self.participants = participants
        self.venue = venue
        self.room = room
        self.organiser = organiser
        self.venue_admin = venue.admin
