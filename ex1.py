 R = 0.0821  # L-atm/K
 T = 500     # K
 V = 5       # L/mol
 Pc = 37.2   # atm
 Tc = 132.5  # K

 a = 0.427 * pow(R,2) * pow(Tc,2.5) / Pc
 b = 0.0866 * R * Tc / Pc

 # Compute in atm
 P_ig = R * T / V
 P_rk = R * T / (V-b) - a/(V*(V+b)*pow(T,0.5))

 # Convert to Pascals
 P_ig = P_ig * 101325
 P_rk = P_rk * 101325

 print("The ideal gas pressure: " + str(P_ig) + " Pa")
 print("The Redlich-Kwong pressure: " + str(P_rk) + " Pa")
