#rituais incomuns
#p(R = sim | H = sim) = 0.90
#p(R = sim | H = não) = 0.10

#contato com estrangeiro
#p(E = sim | H = sim) = 0.80
#p(E = sim | H = não) = 0.20

#silencio na assembléia
#p(S = sim | H = sim) = 0.75
#p(S = sim | H = não) = 0.25

#P(H = sim) = 0.05
#P(H = não) = 0.95

#R = sim
#E = sim
#S = sim


p_SHerege = 0.75
p_SNherege = 0.25

p_EHerege = 0.80
p_EnHerege = 0.20

p_RHerege = 0.90
p_RnHerege = 0.10

p_herege = 0.05
p_nherege = 0.95

p_total_herege = (p_EHerege * p_SHerege * p_RHerege * p_herege) + (p_nherege * p_SNherege * p_RnHerege * p_EnHerege)
print(f"{p_total_herege * 100:.2f}")

p_suspeita = (p_EHerege * p_SHerege * p_RHerege * p_herege) / p_total_herege
print(f"{p_suspeita * 100:.2f}")

#Com base nos sinais indicados foi calculado que a probabildade total de uma pessoa ser herege é de 3,18% e a probabilidade de uma pessoa ser suspeita a partir de cada evidência mostrada aumenta e se torna 85,04%