from application.model.venue.rating import Rating
from application.model.venue.utility.defaults import RoomDefaults


class Room:

    def __init__(self, room_id, name, floor_number, photos, rating_review, other_info, description,
                 schedule, capacity_max, room_amenities, room_type, supported_activities):

        self.room_id = room_id
        self.name = name
        self.floor_number = floor_number
        self.schedule = schedule
        self.rating = Rating(score=rating_review[0], review=rating_review[1])
        self.capacity_max = capacity_max
        self.room_type = room_type
        self.supported_activities = supported_activities
        self.room_amenities = room_amenities
        self.photos = photos
        self.other_info = other_info
        self.description = description


class Classroom(Room):

    def __init__(self, room_id, name, floor_number, photos, rating_review, other_info, description, schedule,
                 capacity_max, room_amenities, supported_activities):

        Room.__init__(self, room_id=room_id, name=name, floor_number=floor_number, photos=photos,
                      rating_review=rating_review, other_info=other_info, description=description,
                      schedule=schedule, capacity_max=capacity_max, room_amenities=room_amenities,
                      room_type=RoomDefaults.TYPE_CLASSROOM, supported_activities=supported_activities)


class SportsHall(Room):

    def __init__(self, room_id, name, floor_number, photos, rating_review, other_info, description, schedule,
                 capacity_max,
                 room_amenities, supported_activities):

        Room.__init__(self, room_id=room_id, name=name, floor_number=floor_number, photos=photos,
                      rating_review=rating_review, other_info=other_info, description=description,
                      schedule=schedule, capacity_max=capacity_max, room_amenities=room_amenities,
                      room_type=RoomDefaults.TYPE_SPORTS_HALL, supported_activities=supported_activities)


class Pitch(Room):

    def __init__(self, room_id, name, floor_number, photos, rating_review, other_info, description, schedule,
                 capacity_max, room_amenities, supported_activities, pitch_size):

        Room.__init__(self, room_id=room_id, name=name, floor_number=floor_number, photos=photos,
                      rating_review=rating_review, other_info=other_info, description=description,
                      schedule=schedule, capacity_max=capacity_max, room_amenities=room_amenities,
                      room_type=RoomDefaults.TYPE_PITCH, supported_activities=supported_activities)

        self.pitch_size = pitch_size


