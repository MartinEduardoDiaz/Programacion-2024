
# A

densidad14 = ("densidad14", round(404432 / 18429, 1))
densidad12 = ("densidad12", round(166533 / 1382291, 1))

R14 = {
    "nombreregion14": "Los Ríos",
    "superficie14": 18429,
    "habitantes14": 404432,
    "densidad14": densidad14
}

R12 = {
    "nombreregion12": "Magallanes",
    "superficie12": 1382291,
    "habitantes12": 166533,
    "densidad12": densidad12
}



R14A = str(R14)
R12A = str(R12)

censo2017 = {
    R14A,
    R12A
}


print()
print(censo2017)
print()




capital = {
    "losrioscapital": "Valdivia",
    "magallanescapital": "Punta Arenas"
}

provincialosrios = ("Valdivia", "Ranco")
provinciamagallanes = ("Antártica Chilena", "Magallanes", "Tierra del Fuego", "Última Esperanza")

provincia = (provincialosrios, provinciamagallanes)


censo2017.update(capital)

R14.update(provincialosrios)
R12.update(provinciamagallanes)


print(censo2017)