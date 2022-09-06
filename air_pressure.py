import math

h_list = range(0, 1000, 10)         #Height (m)
#h_list = [0,10,100,1000]           #Height (m)

#function calculating p_h - pressure at height(h) 
def air_pressure_at_height(h):
    p0 = 101325                     #ref pressure (P)
    L = 0.00976                     #Temp lapse rate
    M = 0.02896968                  #Molar mass of dry air (kg/mol)
    cp = 1004.68506                 #Constant-pressure spec. heat
    g = 9.80665                     #Acceleration due to gravity (m/s^2)
    R0 = 8.314462618                #Universal gas constant (J/mol*K)
    T = 273                         #Temperature (K)

    ratio = -(g * h * M) / (R0 * T)
    p_h = p0 * math.exp(ratio)
    return p_h

for height in h_list:
    p_h = air_pressure_at_height(height)
    print(height, '         ', p_h)
