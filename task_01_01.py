kol_tarelok=int(input())
kol_sredstva=float(input())
kol_vimitih=kol_sredstva/0.5 # сколько тарелок хватит средства
if kol_tarelok>kol_sredstva:
		Print(int(kol_tarelok-kol_vimitih))
elif kol_tarelok<kol_sredstva:
		Print(float((kol_vimitih-kol_tarelok)*0.5))
else:
print('Все тарелки вымыты, средство закончилось') 
