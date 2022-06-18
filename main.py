import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control

bulasik_miktari = control.Antecedent(np.arange(0,101,0.1),"bulasik_miktari")
bulasik_miktari["az"] = fuzzy.trimf(bulasik_miktari.universe, [0,0,35])
bulasik_miktari["orta"] = fuzzy.trimf(bulasik_miktari.universe, [15,50,85])
bulasik_miktari["çok"] = fuzzy.trimf(bulasik_miktari.universe, [65,100,100])

kirlilik_derecesi = control.Antecedent(np.arange(0,101,0.1),"kirlilik_derecesi")
kirlilik_derecesi["az"] = fuzzy.trimf(kirlilik_derecesi.universe, [0,0,35])
kirlilik_derecesi["orta"] = fuzzy.trimf(kirlilik_derecesi.universe, [15,50,85])
kirlilik_derecesi["çok"] = fuzzy.trimf(kirlilik_derecesi.universe, [65,100,100])

bulasik_cinsi = control.Antecedent(np.arange(0,101,0.1),"bulasik_cinsi")
bulasik_cinsi["hassas"] = fuzzy.trimf(bulasik_cinsi.universe, [0,0,35])
bulasik_cinsi["karma"] = fuzzy.trimf(bulasik_cinsi.universe, [15,50,85])
bulasik_cinsi["güçlü"] = fuzzy.trimf(bulasik_cinsi.universe, [65,100,100])

yikama_zamani = control.Consequent(np.arange(30,161,1),"yikama_zamani")
yikama_zamani["çok_kısa"] = fuzzy.trimf(yikama_zamani.universe, [30,30,60])
yikama_zamani["kısa"] = fuzzy.trimf(yikama_zamani.universe, [40,65,90])
yikama_zamani["orta"] = fuzzy.trimf(yikama_zamani.universe, [70,95,120])
yikama_zamani["uzun"] = fuzzy.trimf(yikama_zamani.universe, [100,125,150])
yikama_zamani["çok_uzun"] = fuzzy.trimf(yikama_zamani.universe, [130,160,160])

deterjan_miktari = control.Consequent(np.arange(0,101,0.1),"deterjan_miktari")
deterjan_miktari["çok_az"] = fuzzy.trimf(deterjan_miktari.universe, [0,0,17.5])
deterjan_miktari["az"] = fuzzy.trimf(deterjan_miktari.universe, [7.5,25,42.5])
deterjan_miktari["normal"] = fuzzy.trimf(deterjan_miktari.universe, [32.5,50,67.5])
deterjan_miktari["çok"] = fuzzy.trimf(deterjan_miktari.universe, [57.5,75,92.5])
deterjan_miktari["çok_fazla"] = fuzzy.trimf(deterjan_miktari.universe, [82.5,100,100])

su_sicakligi = control.Consequent(np.arange(35,70,0.1),"su_sicakligi")
su_sicakligi["düşük"] = fuzzy.trimf(su_sicakligi.universe, [35,35,50])
su_sicakligi["normal"] = fuzzy.trimf(su_sicakligi.universe, [37.5,52.5,67.5])
su_sicakligi["yüksek"] = fuzzy.trimf(su_sicakligi.universe, [55,70,70])

ust_sepet_pompa_devri = control.Consequent(np.arange(2100,3500,1),"ust_sepet_pompa_devri")
ust_sepet_pompa_devri["çok_düşük"] = fuzzy.trimf(ust_sepet_pompa_devri.universe, [2100,2100,2400])
ust_sepet_pompa_devri["düşük"] = fuzzy.trimf(ust_sepet_pompa_devri.universe, [2300,2500,2700])
ust_sepet_pompa_devri["orta"] = fuzzy.trimf(ust_sepet_pompa_devri.universe, [2600,2800,3000])
ust_sepet_pompa_devri["yüksek"] = fuzzy.trimf(ust_sepet_pompa_devri.universe, [2900,3100,3300])
ust_sepet_pompa_devri["çok_yüksek"] = fuzzy.trimf(ust_sepet_pompa_devri.universe, [3200,3500,3500])

alt_sepet_pompa_devri = control.Consequent(np.arange(2100,3500,1),"alt_sepet_pompa_devri")
alt_sepet_pompa_devri["çok_düşük"] = fuzzy.trimf(alt_sepet_pompa_devri.universe, [2100,2100,2400])
alt_sepet_pompa_devri["düşük"] = fuzzy.trimf(alt_sepet_pompa_devri.universe, [2300,2500,2700])
alt_sepet_pompa_devri["orta"] = fuzzy.trimf(alt_sepet_pompa_devri.universe, [2600,2800,3000])
alt_sepet_pompa_devri["yüksek"] = fuzzy.trimf(alt_sepet_pompa_devri.universe, [2900,3100,3300])
alt_sepet_pompa_devri["çok_yüksek"] = fuzzy.trimf(alt_sepet_pompa_devri.universe, [3200,3500,3500])

kural1 = control.Rule(
    antecedent = (bulasik_miktari["az"] & kirlilik_derecesi["az"] & bulasik_cinsi["hassas"]),
    consequent = (yikama_zamani["çok_kısa"] , deterjan_miktari['çok_az'] , su_sicakligi['düşük'] , ust_sepet_pompa_devri['çok_düşük'] , alt_sepet_pompa_devri['çok_düşük'])
)

kural2 = control.Rule(
    antecedent = (bulasik_miktari["az"] & kirlilik_derecesi["çok"] & bulasik_cinsi["karma"]),
    consequent = (yikama_zamani["orta"] , deterjan_miktari['normal'] , su_sicakligi['yüksek'] , ust_sepet_pompa_devri['düşük'] , alt_sepet_pompa_devri['çok_yüksek'])
 )

kural3 = control.Rule(
    antecedent = (bulasik_miktari["orta"] & kirlilik_derecesi["orta"] & bulasik_cinsi["güçlü"]),
    consequent = (yikama_zamani["orta"] , deterjan_miktari['normal'] , su_sicakligi['normal'] , ust_sepet_pompa_devri['yüksek'] , alt_sepet_pompa_devri['yüksek'])
 )

kural4 = control.Rule(
    antecedent = (bulasik_miktari["çok"] & kirlilik_derecesi["çok"] & bulasik_cinsi["karma"]),
    consequent = (yikama_zamani["çok_uzun"] , deterjan_miktari['çok_fazla'] , su_sicakligi['yüksek'] , ust_sepet_pompa_devri['düşük'] , alt_sepet_pompa_devri['çok_yüksek'])
 )

control_system = control.ControlSystem([kural1, kural2, kural3, kural4])

system_simulation = control.ControlSystemSimulation(control_system)

system_simulation.input["bulasik_miktari"] = 30
system_simulation.input["kirlilik_derecesi"] = 30
system_simulation.input["bulasik_cinsi"] = 30
system_simulation.compute()

print(system_simulation.output)
yikama_zamani.view(sim= system_simulation)
deterjan_miktari.view(sim= system_simulation)
su_sicakligi.view(sim= system_simulation)
ust_sepet_pompa_devri.view(sim= system_simulation)
alt_sepet_pompa_devri.view(sim= system_simulation)

input()


