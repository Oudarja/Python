class car:
    make=None
    model=None
    year=None
    color=None

    def __init__(self,make,model,year,color):
        self.make=make   
        self.model=model
        self.year=year
        self.color=color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car stopped")
