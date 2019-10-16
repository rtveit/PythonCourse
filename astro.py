class Zodiac:
    
    def __init__(self, name, startBirthMonth, endBirthMonth, startBirthDay,
     endBirthDay  ):
        self.name = name
        self.startBirthMonth = startBirthMonth
        self.endBirthMonth = endBirthMonth
        self.startBirthDay = startBirthDay
        self.endBirthDay = endBirthDay

    def isWithinDate(self,userBirthDay, userBirthMonth):
        

        if userBirthMonth == self.startBirthMonth:
            if  userBirthDay >= self.startBirthDay:
                return True

        if userBirthMonth == self.endBirthMonth:
            if  endBirthDay <= self.endBirthDay:
                return True  

        return False

def main():
    zodiacArray = []
    myFile = open("/home/rob/Dropbox/scripts/astrologyZodiacs.txt")
    print ("hvilen dag er du født på", end= "")
    userBirthDay = input()
    print ("hvilen måned er du født på", end= "")
    userBirthMonth = input()


    for line in range(12):
        name = myFile.readline()
        startBirthMonth = int(myFile.readline())
        endBirthMonth = int(myFile.readline())
        startBirthDay = int(myFile.readline())
        endBirthDay = int(myFile.readline())

        zodiac = Zodiac(name, startBirthMonth, endBirthMonth, startBirthDay,
     endBirthDay)

        zodiacArray.append(zodiac)

        print(userBirthDay) 
        print(userBirthMonth)




        

if __name__ == "__main__":
        main()