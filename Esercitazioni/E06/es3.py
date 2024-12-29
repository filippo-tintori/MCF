import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

URL = "/Users/filippo/Documenti/UniPG/3°Anno/MetodiComputazionaliPerLaFisica/Esercitazioni/E06/oscilloscope.csv"

df = pd.read_csv(URL)

plt.title("Segnali oscilloscopio", color="gray")
plt.plot(df["time"], df["signal1"], color="coral", label="Canale 1")
plt.plot(df["time"], df["signal2"], color="pink", label="Canale 2")
plt.legend()
plt.xlabel("t [ns]")
plt.ylabel("V [mV]")
plt.show()

# f'(i) =  [f(i+n)-f(i-n)] / [x(i+n)-x[i-n]]
def DifferenzaCentrale(x,y,n):
    d = y[n:] - y[:-n]
    h = x[n:] - x[:-n]
    
    for ih in range(int(n/2)):
        d = np.append(y[n-ih-1]-y[0], d)
        d = np.append(d, y[-1]-y[-(n-ih)])
    
        h = np.append(x[n-ih-1]-x[0], h)
        h = np.append(h, x[-1]-x[-(n-ih)])
    
    print('d', d)
    print('h', h)
    return d/h

# derivata con differenza centrale
d100c1 = DifferenzaCentrale(df["time"].to_numpy(), df["signal1"].to_numpy(), 100)
d100c2 = DifferenzaCentrale(df["time"].to_numpy(), df["signal2"].to_numpy(), 100)

plt.title("Derivata Segnali Oscilloscopio con h=100ns", color="gray")
plt.plot(df['time'], d100c1, color='coral',   label='Canale 1')
plt.plot(df['time'], d100c2, color='pink',  label='Canale 2')
plt.legend()
plt.xlabel("t [ns]")
plt.ylabel("V/s [mV/ns]")
plt.show()

der_sig1 = np.convolve(d100c1,  np.ones(5), 'same') / 5
der_sig2 = np.convolve(d100c2,  np.ones(5), 'same') / 5


# Selezione punti con derivata vicina a zero (<0.015) e segnale superiore alla soglia di 10 mV (in negativo)

mask1 = (np.abs(der_sig1)< 0.015) & (df["signal1"].to_numpy() < -10)
mask2 = (np.abs(der_sig2)< 0.015) & (df["signal2"].to_numpy() < -10)

print('---der0 sig1 ---', df['time'].to_numpy()[mask1])
print('---der0 sig2 ---', df['time'].to_numpy()[mask2])

tsig1 = np.empty(0)
vsig1 = np.empty(0)
tsum = df["time"].to_numpy()[mask2][0]
nsum=1

for it in range( 1, len(df['time'].to_numpy()[mask1])):
    if ( (df['time'].to_numpy()[mask1][it]-df['time'].to_numpy()[mask1][it-1]) > 20)  or (it == (len(df['time'].to_numpy()[mask1]))-1):
        print(tsum)
        tsig1 = np.append( tsig1, tsum)
        vsig1 = np.append( vsig1, df['signal1'].to_numpy()[tsum] )
        tsum = df['time'].to_numpy()[mask1][it]

tsig2 = np.empty(0)
vsig2 = np.empty(0)
tsum = df['time'].to_numpy()[mask2][0]
nsum = 1

for it in range( 1, len(df['time'].to_numpy()[mask2])):
    if ( (df['time'].to_numpy()[mask2][it]-df['time'].to_numpy()[mask2][it-1]) > 20 ) or it == ( len(df['time'].to_numpy()[mask2]))-1 :
        tsig2 = np.append( tsig2, tsum)
        vsig2 = np.append( vsig2, df['signal2'].to_numpy()[tsum] )
        tsum = df['time'].to_numpy()[mask2][it]


plt.title('Segnali Oscilloscopio con Minimi identificati', fontsize=16, color='slategray')
plt.plot( df['time'].to_numpy(), df['signal1'].to_numpy(), color='limegreen',  label='Canale 1' )
plt.plot( df['time'].to_numpy(), df['signal2'].to_numpy(), color='darkorange', label='Canale 2' )
plt.plot( tsig1, vsig1, 'o', color='darkgreen',  label='Min. Canale 1' )
plt.plot( tsig2, vsig2, 'o', color='red',        label='Min. Canale 2' )
plt.legend(fontsize=14)
plt.xlabel('t [ns]')
plt.ylabel('V [mV]')
plt.ylim(-90, 10)
plt.show()

tcoin1 = np.empty(0)
tcoin2 = np.empty(0)
vcoin1 = np.empty(0)
vcoin2 = np.empty(0)
window = 200
for t1, v1 in zip(tsig1, vsig1):
    for t2, v2 in zip(tsig2, vsig2):
        if np.abs(t2-t1) < window:
            tcoin1 = np.append(tcoin1, t1)
            tcoin2 = np.append(tcoin2, t2)
            vcoin1 = np.append(vcoin1, v1)
            vcoin2 = np.append(vcoin2, v2)
        if t2 > t1 :
            break

#################  Stampa risultati coincidenze  ##################### 
print('--------------------------------------------')
print(' Numero Coincidenze        :', len(tcoin1) )
print(' Tempo Coincidenze Canale 1:', tcoin1)
print(' Tempo Coincidenze Canale 2:', tcoin2)
print(' Coincidenze t2-t1         :', tcoin2-tcoin1)
print(' Efficenza Canale 1        : {:.2f}'.format( len(tcoin1)/len(tsig2)) )
print(' Efficenza Canale 2        : {:.2f}'.format( len(tcoin2)/len(tsig1)) )