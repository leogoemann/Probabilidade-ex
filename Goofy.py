
#EMOJIS COLORIDOS
# P(E=sim | K=sim) = 0.85
# P(E=sim | K=não) = 0.15

#IDOLS
#P(L = sim | K = SIM) = 0.95
#P(L = SIM | K = NÃO) = 0.05

#MOLETOM
#P(C = SIM | K = SIM) = 0.90
#P(C = SIM | K = NÃO) = 0.10

# P(K = SIM) = 0.07
# P(K = NÃO) = 0.93


#E =SIM
#L = SIM
#C = SIM

p_Eskpop = 0.85
p_Enkpop = 0.15

p_Lskpop = 0.95
p_Lnkpop = 0.05

p_Cskpop = 0.90
p_Cnkpop = 0.10

p_kpop = 0.07
p_nkpop = 0.93

p_total = (p_Eskpop * p_Lskpop * p_Cskpop * p_kpop) + (p_Enkpop * p_Lnkpop * p_Cnkpop * p_nkpop)
print(f"{p_total * 100:.2f}")

p_suspeita = (p_Eskpop * p_Lskpop * p_Cskpop * p_kpop) / p_total
print(f"{p_suspeita * 100:.2f}")

#Com base nos sinais indicados foi calculado que a probabildade total do goofy ser fã de kpop é de 3,18% e a probabilidade dele ser suspeito a partir de cada evidência mostrada aumenta se torna 85,04%