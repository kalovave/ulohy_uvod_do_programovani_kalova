# Výpis počtu samohlásek a souhlásek v textu
# Veronika Kalová, 2. ročník, obor Geografie a kartografie
# ZS 2025/2026
# Úvod do programování (MZ370P19)


# creating a class for text analysis
class TextAnalysis:
    def __init__(self, input):
        self.input = input
        self.__vowels = ["a", "e", "i", "o", "u", "y", "á", "ě", "í", "ó", "ú", "ů", "ý"]   # definition of Czech vowels
        self.__number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__spec_char = [",", ".", "?", "!", ";"]   # definion of special characters
        self.new = []   # creating a list

    def open_input(self):
        try:
            with open(self.input, encoding="utf-8") as f:   # opening a document with encoding that supports Czech alphabet
                vowel_count = 0   # setting the counters
                cons_count = 0   
                number_count = 0
                spec_count = 0
                space = 0

                for line in f:   # reading the document by lines
                    for char in line.lower():   # reading the lines by characters
                        if char in self.__number:
                            number_count = number_count + 1   # adding +1 to number counter when finding a number
                        elif char in self.__spec_char:
                            spec_count = spec_count + 1   # adding +1 to special character counter when finding a special character
                        elif char == " ":
                            space = space + 1
                        else:
                            if char.isalpha():   # identifying letters from special "banned" characters (plus, minus, semiolon etc.)
                                if char in self.__vowels:
                                    vowel_count = vowel_count + 1   # adding +1 to vowel counter when finding a vowel
                                else:
                                    cons_count = cons_count + 1   # adding +1 to consonant counter when finding a consonant

                        self.new.append(char) # adding characters to the list

                self.counting(vowel_count, cons_count, number_count, spec_count, space)   # calling a method for percentage counting

        # error patches
        except FileNotFoundError:
            print(f"Error, input not found.")
            exit()
        except Exception as e:
            print(f"Unexpected error: {e}")
        
    # percentage counting
    def counting(self, vowel_count, cons_count, number_count, spec_count, space):
        self.__vowel_count = vowel_count
        self.__cons_count = cons_count
        self.__number_count = number_count
        self.__spec_count = spec_count
        self.__space = space
        self.__length = self.__vowel_count + self.__cons_count + self.__number_count + self.__spec_count + self.__space   # counting the lenght of the text

        if self.__length > 0:
            self.vowel_perc = (self.__vowel_count/self.__length)*100   # counting the percantage only if the text has more than 0 letters
            self.cons_perc = (self.__cons_count/self.__length)*100     # percentage = (vowels or consonants count)/character count * 100
        else:
            self.vowel_perc = 0   # making sure the document is not empty
            self.cons_perc = 0

    # printing the results into the console
    def print_output(self):
        if self.__length > 0:
            print(f"Soubor s analýzou textu byl vytvořen.")
        else:
            print(f"Textový soubor neobsahuje žádná písmena.")   # if the document has not letters, the programme prints this warning
            exit()

    # method for creating output document
    def output_document(self):
        with open (r"vysledky2.txt", "w", encoding="utf-8") as document:
            for char in self.new:
                document.write(char)   # writing all the characters into the new document
            document.write(f"\n\nTextový soubor obsahuje {self.__length} znaků, z toho {self.__vowel_count} samohlásek ({self.vowel_perc:.2f} %) a {self.__cons_count} souhlásek ({self.cons_perc:.2f} %).")


input = r"uloha_2.txt"

output = TextAnalysis(input)
output.open_input()
output.print_output()
output.output_document()   