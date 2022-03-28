import matplotlib
import matplotlib.pyplot as plt
x_koord=[2000,2005,2010,2015,2020,2025,2030]#gadi
y_koord=[2,4,5,7,8,10,12]#lati kabata
y_koord2=[5,8,2,5,6,7.50,4.20]#lati nopelniti h
#plt.style.use("seaborn")
plt.xlabel("Gadi")
plt.ylabel("Darbi strādāti")
plt.title("Darbi strādāti pa 30 gadiem")
plt.plot(x_koord,y_koord,label="Darbi",linewidth=4,color="mediumspringgreen")
plt.plot(x_koord,y_koord2,label="Lati nopelniti stundā",linewidth=4,color="sienna")
plt.legend(loc="upper left")
plt.show()#vienmer pedeja rinda