from application.model.event.utility.defaults import EventDefaults
from application.model.venue.venue import Venue


class Event:

    def __init__(self, event_id, event_name, venue, max_capacity, participants, room, organiser, event_type,
                 activity, rating_review, other_info, description):

        self.event_id = event_id
        self.event_name = event_name
        self.max_capacity = max_capacity
        self.participants = participants
        self.venue = venue
        self.room = room
        self.organiser = organiser
        self.venue_admin = venue.admin
        self.event_type = event_type
        self.activity = activity
        self.rating_review = rating_review
        self.other_info = other_info
        self.description = description


class SportsEvent(Event):

    def __init__(self, event_id, event_name, venue, max_capacity, participants, room, organiser, activity,
                 rating_review, other_info, description):

        Event.__init__(self, event_id=event_id, event_name=event_name, venue=venue, max_capacity=max_capacity,
                       participants=participants, room=room, organiser=organiser, event_type=EventDefaults.TYPE_SPORTS,
                       activity=activity, rating_review=rating_review, other_info=other_info, description=description)


class AcademicEvent(Event):

    def __init__(self, event_id, event_name, venue, max_capacity, participants, room, organiser, activity,
                 rating_review, other_info, description):

        Event.__init__(self, event_id=event_id, event_name=event_name, venue=venue, max_capacity=max_capacity,
                       participants=participants, room=room, organiser=organiser,
                       event_type=EventDefaults.TYPE_ACADEMIC, activity=activity, rating_review=rating_review,
                       other_info=other_info, description=description)


class ReligiousEvent(Event):

    def __init__(self, event_id, event_name, venue, max_capacity, participants, room, organiser, activity,
                 rating_review, other_info, description):

        Event.__init__(self, event_id=event_id, event_name=event_name, venue=venue, max_capacity=max_capacity,
                       participants=participants, room=room, organiser=organiser,
                       event_type=EventDefaults.TYPE_RELIGIOUS, activity=activity, rating_review=rating_review,
                       other_info=other_info, description=description)
