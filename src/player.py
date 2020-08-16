# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, age, current_room):
        self.name = name
        self.age = age
        self.current_room: Room = current_room
