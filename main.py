# ejena_black
class Student:
    # [assignment] Skeleton class. Add your code here
    # The init method or constructor
    def __init__(self, name, age, tracks, score):
        self.name   = name
        self.age    = int(age)
        self.tracks = tracks
        self.score  = float(score)
    
    # Change name variable
    def change_name(self, name):
        self.name = name

    # Change age variable
    def change_age(self, age):
        self.age = int(age)

    # Add to track variable
    def add_track(self, track):
        self.tracks.append(track)

    # Retrieve score variable
    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
