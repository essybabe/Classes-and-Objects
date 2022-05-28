


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,scores):
        self.name = name
        self.age =age
        self.tracks = tracks
        self.scores = scores

    def change_name(self, name):
        self.name = name
    
    def change_age(self, age):
        self.age = age

    def change_tracks(self, tracks):
        self.tracks = tracks

    def change_scores(self):
        self.scores 

    def Display(self):
        print(self.name)
        print(self.age)
        print(self.tracks)
        print(self.scores)
    
    
   



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],scores=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.change_tracks("UI/UX")
Bob.change_scores()

Bob.Display()