class Zodiac:        
	def __init__(self, name, startBirthMonth, 
		endBirthMonth, startBirthDay, endBirthDay):
		self.name = name        
		self.startBirthMonth = startBirthMonth        
		self.endBirthMonth = endBirthMonth        
		self.startBirthDay = startBirthDay        
		self.endBirthDay = endBirthDay

	def isWithinDate(self, userBirthDay, userBirthMonth):
		if userBirthMonth == self.startBirthMonth:
			if userBirthDay >= self.startBirthDay:
				return True

		if userBirthMonth == self.endBirthMonth:
			if userBirthDay <= self.endBirthDay:
				return True

		return False

def main():
	zoidacFile = open("astrologyZodiacs.txt")
	zodiacArray = []
	for i in range(12):
		name = zoidacFile.readline()
		startBirthMonth = int(zoidacFile.readline())
		startBirthDay = int(zoidacFile.readline())
		endBirthMonth = int(zoidacFile.readline())
		endBirthDay = int(zoidacFile.readline())

		zodiac = Zodiac(name, startBirthMonth, 
			endBirthMonth, startBirthDay, endBirthDay)
		zodiacArray.append(zodiac)

if __name__ == "__main__":
	main()