# Výpočet mediánu pro nesetříděnou posloupnost tvořenou n prvky
# Veronika Kalová, 2. ročník, obor Geografie a kartografie
# ZS 2025/2026
# Úvod do programování (MZ370P19)


# creating a class for median counting
class Median:
    def __init__(self, input):
        self.input = input
        self.sorted = []   # creating a list for sorted numbers
        self.median = 0   # setting a median

    def open_input(self):
        try:
            with open(self.input, encoding="utf-8") as f:   # document opening
                for line in f:   # reading the document by lines                  
                    numbers = line.split(";")   # splitting the numbers with ";"
                    for number in numbers:
                        if number.strip():   # making sure the programme is working despite two ";" eisting in the document
                            self.sorted.append(int(number))   # rewritting the numbers from str to int
  
        # error patches
        except FileNotFoundError:
            print(f"Error, input not found.")   # error - wrong separator between numbers (".", "-", " ", etc.)
            exit()
        except ValueError:
            print(f"Chyba, invalid data.")   # document contains different characters instead of just numbers and separators
            exit()
        except Exception as e:
            print(f"Unexpected error: {e}")

    def sort(self):
        self.__length = len(self.sorted)
        for i in range(self.__length):   # bubble sort - for each number in the range number count
            for j in range (0, self.__length - i - 1):   # for each number in range from 0 to (lenght - i - 1)
                if self.sorted[j] > self.sorted[j + 1]:   # if the number on the first place is bigger than the next one, switch them
                    self.sorted[j], self.sorted[j + 1] = self.sorted[j + 1], self.sorted[j]

        self.find_median()

    def find_median(self):
        if self.__length == 0:   # if the document has no numbers, print the warning
            print(f"Textový soubor neobsahuje platné čísice.")
            exit()
        elif (self.__length % 2) == 0:
            i = (self.__length // 2) - 1
            j = self.__length // 2
            self.median = (self.sorted[i] + self.sorted[j])/2   # counting the median for even numbers - the mean of the middle numbers
        else:
            i = self.__length // 2
            self.median = self.sorted[i]   # the mediean for odd numbers - the middle number

    # creating the output
    def print_output(self):
        with open (r"vysledky94.txt", "w", encoding="utf-8") as document:
            for number in self.sorted:      # writing all the numbers from "self.sorted"
                document.write(f"{number}\n")
            document.write(f"\n\nMedián nesetříděné posloupnosti je {self.median}.")

        print(f"Soubor s analýzou celočíselné posloupnosti byl vytvořen.")


input = r"uloha_94.txt"

output = Median(input)
output.open_input()
output.sort()
output.print_output()