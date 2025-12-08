class student:
    def __init__(self, name, rollNumber, M1, M2, M3):
        self.name = name
        self.rollNumber = rollNumber
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3

    def totalMarks(self):
        total = self.M1 + self.M2 + self.M3
        print("Total Marks:", total)
        print("Percent:", total / 3)
        return total    

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollNumber)
        print("Marks1:", self.M1)
        print("Marks2:", self.M2)
        print("Marks3:", self.M3)

        total = self.M1 + self.M2 + self.M3 
        print("Percent:", total / 3)         

        self.totalMarks()

s1 = student("Manan Jain", 20, 85, 90, 95)
s1.display()