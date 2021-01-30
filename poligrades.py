import re
import sys
import matplotlib.pyplot as plt

REGEXP = r"([0-9]{6})\s+?(30 e Lode|[0-9]{2}|RIMANDATO|ASSENTE|RIPROVATO)\s+?([0-9]{6}) - (.+?)\s+\(\s*?CFU:\s*?([0-9]{1,2})\s*?\)"
persone = 0
assenti = 0
rimandati = 0
riprovati = 0
sommaVoti = 0
voti = []

with open('elettronica.txt','r') as f_open:
    results = f_open.read().strip().split("\n")
    for line in results:
        match = re.findall(REGEXP, line)[0]
        matricola = int(match[0])
        cod_insegnamento = int(match[2])
        dsc_insegnamento = match[3]
        cfu = int(match[4])

        try:
            valutazione = int(match[1])
            persone = persone + 1
            sommaVoti = sommaVoti + valutazione
            voti.append(valutazione)

        except ValueError:
            if (match[1] == "30 e Lode"):
                valutazione = 30
                persone = persone + 1
                sommaVoti = sommaVoti + valutazione
                voti.append(valutazione)

            elif (match[1] == "ASSENTE"):
                valutazione = None
                assenti = assenti + 1

            elif (match[1] == "RIMANDATO"):
                valutazione = 0
                rimandati = rimandati + 1

            elif (match[1] == "RIPROVATO"):
                valutazione = 0
                riprovati = riprovati + 1

media = sommaVoti / persone 
data = input("Inserire data [mese-anno] svolgimento esame: ")
print("Nome Materia: " + dsc_insegnamento)	
print("CFU: " + str(cfu))
print("Media Voti " + str(round(media, 2)))
print("Persone che hanno fatto l'esame: "+ str(persone + rimandati + riprovati))
print("Numero Rimandati " + str(rimandati))
print("Numero Assenti " + str(assenti))
print("Numero Riprovati " + str(riprovati))

scelta = input("Vuoi salvare i dati in un file? [S], [N]: ")
if (scelta == 'S' or scelta == 's'):
    SavedGrades = open("SavedGrades.txt", mode='a+', encoding='utf-8')
    SavedGrades.write(dsc_insegnamento + " - " + data + "\n")
    SavedGrades.write("CFU: " + str(cfu)+ "\n")
    SavedGrades.write("Media Voti " + str(round(media, 2))+ "\n")
    SavedGrades.write("Persone che hanno fatto l'esame: "+ str(persone + rimandati + riprovati)+ "\n")
    SavedGrades.write("Numero Rimandati " + str(rimandati)+ "\n")
    SavedGrades.write("Numero Assenti " + str(assenti)+ "\n")
    SavedGrades.write("Numero Riprovati " + str(riprovati)+ "\n")
    SavedGrades.close()

 
voti.sort()
plt.hist(voti, bins=13) #plot the data
plt.ylabel('Frequenza') #set the label for y axis
plt.xlabel('Voti') #set the label for x-axis
plt.title(dsc_insegnamento + " - " + data) #set the title of the graph
plt.savefig('plot.png')
plt.show() #display the graph

plt.close()

