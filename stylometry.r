# učitavanje biblioteke stylo

library("stylo")

# podešavanje radnog direktorijuma
setwd("/Users/ljudmilapetkovic/stilometrija/autor_pesme_album/autor_pesme")

# standardno korišćenje (kreira korpus od skupa tekstualnih datoteka) i poziva GUIS
stylo()

# kreira korpus od skupa datoteka sa zadatim parametrima i daje rezultat
stylo(gui = F, mfw.min = 1000, mfw.max = 5000)