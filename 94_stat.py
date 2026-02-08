# Výpočet mediánu pro nesetříděnou posloupnost tvořenou n prvky
# Veronika Kalová, 2. ročník, obor Geografie a kartografie
# ZS 2025/2026
# Úvod do programování (MZ370P19)


# tvorba třídy pro výpočet mediánu z nesetříděné posloupnosti
class Median:
    def __init__(self, vstup):
        self.vstup = vstup
        self.serazeni = []   # tvorba listu pro zapsání čísel a jejich následnou práci s nimi
        self.vysledny_median = 0   # nastavení mediánu souboru čísel na 0

    def otevri_soubor(self):
        try:
            with open(self.vstup, encoding="utf-8") as f:   # otevření souboru
                for radek in f:   # čtení řádku
                    radek = radek.strip()   # zbavení řádku zbytečných mezer (v případdě, kdyby číslia byla ve více řádcích)
                    if not radek:   # přeskočení řádku, pokud nic neobsahuje
                        continue
                    
                    cisla = radek.split(";")   # rozdělení čísel středníkem
                    for cislo in cisla:
                        if cislo.strip():   # ošetření vstupních dat - kdyby se ve vstupu objevily dva oddělovače za sebou
                            self.serazeni.append(int(cislo))   # přepis čísel z str na int
  
        # ošetření errorů
        except FileNotFoundError:
            print(f"Chyba, vstupní soubor nebyl nalezen.")   # ošetření špatných oddělovačů mezi číslicemi posloupnosti (např. teček, mezer...)
            exit()
        except ValueError:
            print(f"Chyba, dokument obsahuje neplatná data.")   # dokument obsahuje i jiné znaky než poze číslice (např. mezery nebo písmena)
            exit()
        except Exception as e:
            print(f"Neočekávaná chyba: {e}")

    def serad(self):
        self.__delka = len(self.serazeni)
        for i in range(self.__delka):   # bubble sort - pro každé číslo v rozsahu počtu číslic
            for j in range (0, self.__delka - i - 1):   # pro každé číslo v rozsahu od 0 až (délka - i - 1)
                if self.serazeni[j] > self.serazeni[j + 1]:   # pokud je číslo dřív v pořadí větší než číslo následující, prohoď jejich hodnoty
                    self.serazeni[j], self.serazeni[j + 1] = self.serazeni[j + 1], self.serazeni[j]

        self.najdi_median()

    def najdi_median(self):
        if self.__delka == 0:   # pokud soubor obsahuje nula číslic, vypiš chybovou hlášku
            print(f"Textový soubor neobsahuje platné čísice.")
            exit()
        elif (self.__delka % 2) == 0:
            i = (self.__delka // 2) - 1
            j = self.__delka // 2
            self.vysledny_median = (self.serazeni[i] + self.serazeni[j])/2   # výpočet medián pro sudý počet čísel - průměr dvou prostředních hodnot
        else:
            i = self.__delka // 2
            self.vysledny_median = self.serazeni[i]   # výpočet medián pro lichý počet čísel - určení prostřední hodnoty

    # tvorba výsledného dokumentu
    def tisk_vysledku(self):
        with open (r"vysledky94.txt", "w", encoding="utf-8") as dokument:
            for cislo in self.serazeni:      # do nového dokumentu vepíšeme každé seřazené číslo ze seznamu "self.serazeni"
                dokument.write(f"{cislo}\n")
            dokument.write(f"\n\nMedián nesetříděné posloupnosti je {self.vysledny_median}.")

        print(f"Soubor s analýzou celočíselné posloupnosti byl vytvořen.")


vstup = r"uloha_94.txt"

vystup = Median(vstup)
vystup.otevri_soubor()
vystup.serad()
vystup.tisk_vysledku()