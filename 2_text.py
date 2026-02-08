# Výpis počtu samohlásek a souhlásek v textu
# Veronika Kalová, 2. ročník, obor Geografie a kartografie
# ZS 2025/2026
# Úvod do programování (MZ370P19)


# tvorba třídy pro analýzu samohlásek a souhlásek textu
class AnalyzaTextu:
    def __init__(self, vstup):
        self.vstup = vstup
        self.__samohlasky = ["a", "e", "i", "o", "u", "y", "á", "ě", "í", "ó", "ú", "ů", "ý"]   # definice českých samohlásek
        self.__cisla = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__spec_znaky = [",", ".", "?", "!", ";"]   # definice speciálních znaků, které nemají být ignorovány
        self.novy_soubor = []   # vytvoření seznamu pro pozdější zapsání do nového dokumentu

    def otevri_soubor(self):
        try:
            with open(self.vstup, encoding="utf-8") as f:   # otevření souboru s encodingem 
                samohl_pocet = 0   # základní nastavení počítadel
                souhl_pocet = 0   
                cisla_pocet = 0
                spec_pocet = 0
                mezery = 0

                for radek in f:   # čtení souboru po řádcích
                    for znak in radek.lower():   # čtení souboru po znacích a vyřešení citlivosti pro velká a malá písmena
                        if znak in self.__cisla:
                            cisla_pocet = cisla_pocet + 1   # při nalezení čísla se počítadlo navýší o 1
                        elif znak in self.__spec_znaky:
                            spec_pocet = spec_pocet + 1   # při nalezení zadaného specifického znaku se počítadlo navýší o 1
                        elif znak == " ":
                            mezery = mezery + 1
                        else:
                            if znak.isalpha():   # rozlišení písmen od číslic, mezer a speciálních znaků
                                if znak in self.__samohlasky:
                                    samohl_pocet = samohl_pocet + 1   # při nalezení samohlásky se počítadlo navýší o 1
                                else:
                                    souhl_pocet = souhl_pocet + 1   # při nalezení souhlásky se počítadlo navýší o 1

                        self.novy_soubor.append(znak) # zápis znaku do listu pro následné přepsání do nového souboru

                self.prepocet(samohl_pocet, souhl_pocet, cisla_pocet, spec_pocet, mezery)   # volání metody třídy, která vypočítává procentuální zastoupení samohlásek a souhlásek

        # ošetření errorů
        except FileNotFoundError:
            print(f"Chyba, vstupní soubor nebyl nalezen.")
            exit()
        except Exception as e:
            print(f"Neočekávaná chyba: {e}")
        
    # výpočet procent
    def prepocet(self, samohl_pocet, souhl_pocet, cisla_pocet, spec_pocet, mezery):
        self.__samohl_pocet = samohl_pocet
        self.__souhl_pocet = souhl_pocet
        self.__cisla_pocet = cisla_pocet
        self.__spec_pocet = spec_pocet
        self.__mezera = mezery
        self.__delka = self.__samohl_pocet + self.__souhl_pocet + self.__cisla_pocet + self.__spec_pocet + self.__mezera   # výpočet počtu znaků v souboru, prvek nutný pro výpočet procentuálního zastoupení

        if self.__delka > 0:
            self.samohl_proc = (self.__samohl_pocet/self.__delka)*100   # výpočet procentuálního zastoupení za podmínky, že soubor obsahuje více než 0 znaků
            self.souhl_proc = (self.__souhl_pocet/self.__delka)*100     # procenta = (počet samohlásek nebo souhlásek)/počet znaků * 100
        else:
            self.samohl_proc = 0   # ošetření prázdného souboru
            self.souhl_proc = 0

    # metoda pro tisk výsledků do konzole
    def tisk_vysledku(self):
        if self.__delka > 0:
            print(f"Soubor s analýzou textu byl vytvořen.")
        else:
            print(f"Textový soubor neobsahuje žádná písmena.")   # pokud soubor neobsahuje žádná písmena, vytiskne se upozornění
            exit()

    # tvorba metody tvořící výstupní data v novém textovém souboru
    def vystupni_soubor(self):
        with open (r"vysledky2.txt", "w", encoding="utf-8") as dokument:
            for znak in self.novy_soubor:
                dokument.write(znak)   # napiš každý znak v novém souboru
            dokument.write(f"\n\nTextový soubor obsahuje {self.__delka} znaků, z toho {self.__samohl_pocet} samohlásek ({self.samohl_proc:.2f} %) a {self.__souhl_pocet} souhlásek ({self.souhl_proc:.2f} %).")


vstup = r"uloha_2.txt"

vystup = AnalyzaTextu(vstup)
vystup.otevri_soubor()
vystup.tisk_vysledku()
vystup.vystupni_soubor()   