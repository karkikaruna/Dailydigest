import matplotlib.pyplot as plt
import numpy as np

R = float(input("Enter Resistance R(ohm): "))
C = float(input("Enter Capacitance C (F) : "))
q_initial = float(input("Enter Initial charge q0 (C): "))
t_final = float(input("Enter Final time tf (s): "))
h = float(input("Enter Step size h: "))

time = np.arange(0, t_final + h, h)
q = np.zeros(len(time))
q[0] = q_initial

def discharge(time, q):
    return -q/(R*C)


for i in range(len(time)-1):
    k1 = h * discharge(time[i], q[i])
    k2 = h * discharge(time[i] + h/2, q[i] + k1/2)
    q[i+1] = q[i] + k2

q_actual = q_initial * np.exp(-time/(R*C))
 
print("\nRC Circuit Discharging\n")
print(" Time(s)\t RK2 Charge (C) \t Analytical Charge(C)")
for i in range(len(time)):
    print(f"{time[i]:.2f} \t\t {q[i]:.4f} \t\t {q_actual[i]:.4f}")

plt.figure(figsize = (8,5))
plt.plot(time, q, color = 'b', marker ='o', linestyle ='-', 
         label = 'RK2 Solution')
plt.plot(time, q_actual, color ='r', linestyle = '--', 
         label = 'Analytical Solution')
plt.title("Capacitor Discharging")
plt.xlabel("Time (s)")
plt.ylabel("Charge q(t) (C)")
plt.legend()
plt.grid(True)
plt.show()

