class Car:
    def ride(self):
        print("Riding a car!")


class Boat:
    def swim(self):
        print("Swimming a boat!")


class MusicMixin:
    def play(self, song):
        print("Now playing: {}".format(song))


class CarBoat(Car, Boat, MusicMixin):
    pass;
