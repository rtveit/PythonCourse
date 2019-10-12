
def mate(vektGramHundeMat, hundeMatSpist):
	print("Skriv antall gram hundemat: ", end = "")
	vektGramHundeMat = int(input())
	return hundeMatSpist + vektGramHundeMat

def gaTur(navaerendeDistanse, avstandGaTur):
	print("Skriv antall kilometer for turen: ", end = "")
	avstandGaTur = int(input())
	return navaerendeDistanse + avstandGaTur

def bjeff():
	print("Voff!")

def main():
	distanse = 0
	hundeMatSpist = 0
	print("Skriv inn navn på hunde: ", end="")
	hundeNavn = input()

	while True:
		print("Skriv inn kommando for " + hundeNavn + ": ", end = "")
		kommando = input()

		if kommando == "bjeff":
			bjeff()

		elif kommando == "Gå Tur":
			distanse = gaTur(distanse, avstandGaTur)
			print(hundeNavn + " har gått totalt: " + str(distanse) + "km")

		elif kommando == "Mate":
			if(hundeMatSpist >= 1000):
				print(hundeNavn + " er veldig mett og vil ikke spise mer")
			else:
				hundeMatSpist = mate(vektGramHundeMat, hundeMatSpist)
				print(hundeNavn + " har " + str(hundeMatSpist) + "g i magen")



if __name__ == '__main__':
	main()