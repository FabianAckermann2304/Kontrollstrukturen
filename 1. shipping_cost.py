VERSANDPAUSCHALE = 5.50
FREIGRENZE = 200

bestellwert = float(input("Bitte geben sie den Bestellwert ein: "))

if bestellwert >= FREIGRENZE:
    rechnungsbetrag = bestellwert
else:
    rechnungsbetrag = VERSANDPAUSCHALE+bestellwert
print("Rechnungsbetrag = ", rechnungsbetrag)

