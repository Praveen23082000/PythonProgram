
class Movie:
    title:str
    rating:int
    run_time:int
    direction:str
    genre:str
    def set_movie(self,title,rating,run_time,direction,genre):

        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.direction=direction
        self.genre=genre
    def set_display(self):

        print(self.title,self.rating,self.run_time,self.direction,self.genre)
arm=Movie()
kgf=Movie()
arm.set_movie("arm",4.2,"2:30","jithin lal","action")
kgf.set_movie("kgf",4.5,"3hour","prasanth nil","action")
arm.set_display()
kgf.set_display()


