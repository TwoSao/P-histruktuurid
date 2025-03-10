sõne = "Programeerimine"
print(sõne)
sõne_list=list(sõne)
sõne_list.reverse()
print(sõne_list)
print(sõne_list[-1])
countl=sõne_list.count("m")
for i in range(countl):
    sõne_list.remove("m")
print(sõne_list)

