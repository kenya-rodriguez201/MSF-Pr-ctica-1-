"""
Práctica 1: CapÌtulo 5
ExperimentaciÛn
in silico
: Modelizado,
an·lisis y control de sistemas ÖsiolÛgicos

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Jeanette Cubillas Arteaga
Número de control: 20212948
Correo institucional: l20212948@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np 
import math as m 
import matplotlib.pyplot as plt 
import control as ctrl

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,6,3
N = round((tend-t0)/dt+1)
t = np.linspace(t0,tend,N)
u1 = np.ones(N)#Escalon punta
u2 = np.zeros(N); u2[round(1/dt):round(2/dt)]= 1 #Impulso 
u3 = (np.linspace(0,tend,N))/tend #Rampa con pendiente 1/10
u4 = np.sin(m.pi/2*t) #Funcion sinusoidal, pi/2 = 250 mH

u = np.stack((u1,u2,u3,u4), axis = 1)
signal = ['Escalon', 'Impulso','Rampa','Sin']

# Componentes del circuito RLC y función de transferencia
R = 10E3
L = 10E-3
C = 47E-6
num = [C*L*R,C*R**2*+L,R]
den = [3*C*L*R,5*C*R**2+L,2*R]
sys = ctrl.tf(num,den)
print (sys)

# Componentes del controlador I
Cr = 1E-6
kI= 304.7921
Re = 1/(kI*Cr); print('Re = ', Re)
numPID = [1]
denPID = [Re*Cr]
PID = ctrl.tf(numPID,denPID)
print(PID)

# Sistema de control en lazo cerrado
X = ctrl.series(PID,sys)
sysPID = ctrl.feedback(X,1, sign = -1)
print(sysPID)

# Respuesta del sistema en lazo abierto y en lazo 
#Morado: [70/255,53/255,177/255]
#Verde: [62/255,123/255,39/255]
#Rosa: [255/255, 116/255, 139/255]
#Azul: [7/255, 71/255, 153/255]

fig1 = plt.figure();
plt.plot(t,u1,'-',color = [70/255,53/255,177/255],label ='Ve(t)')
_,PA = ctrl.forced_response(sys,t,u1,x0)
plt.plot(t,PA, '-', color = [62/255,123/255,39/255], label ='Vs(t)'  )
_,VPID = ctrl.forced_response(sysPID,t,u1,x0)
plt.plot(t,VPID, ':', linewidth = 2, color = [255/255, 116/255, 139/255], label ='VPID(t)'  )
plt.xlim(-0.25,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(0,1.02); plt.yticks(np.arange(0,1.1,0.1))
plt.xlabel('t [s]', fontsize = 11)
plt.ylabel('Vi(t) [V]', fontsize = 11)
plt.legend(bbox_to_anchor = (0.5, -0.2), loc = 'center', ncol = 3, fontsize = 8, frameon = False)
plt.show()
fig1.savefig('step.pdf', bbox_inches = 'tight')

fig2 = plt.figure();
plt.plot(t,u2,'-',color = [70/255,53/255,177/255],label ='Ve(t)')
_,PA = ctrl.forced_response(sys,t,u2,x0)
plt.plot(t,PA, '-', color = [62/255,123/255,39/255], label ='Vs(t)'  )
_,VPID = ctrl.forced_response(sysPID,t,u2,x0)
plt.plot(t,VPID, ':', linewidth = 2, color = [255/255, 116/255, 139/255], label ='VPID(t)'  )
plt.xlim(-0.25,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(0,1.02); plt.yticks(np.arange(0,1.1,0.1))
plt.xlabel('t [s]', fontsize = 11)
plt.ylabel('Vi(t) [V]', fontsize = 11)
plt.legend(bbox_to_anchor = (0.5, -0.2), loc = 'center', ncol = 3, fontsize = 8, frameon = False)
plt.show()
fig2.savefig('pulse.pdf', bbox_inches = 'tight')

fig3 = plt.figure();
plt.plot(t,u3,'-',color = [70/255,53/255,177/255],label ='Ve(t)')
_,PA = ctrl.forced_response(sys,t,u3,x0)
plt.plot(t,PA, '-', color = [62/255,123/255,39/255], label ='Vs(t)'  )
_,VPID = ctrl.forced_response(sysPID,t,u3,x0)
plt.plot(t,VPID, ':', linewidth = 2, color = [255/255, 116/255, 139/255], label ='VPID(t)'  )
plt.xlim(-0.25,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(0,1.02); plt.yticks(np.arange(0,1.1,0.1))
plt.xlabel('t [s]', fontsize = 11)
plt.ylabel('Vi(t) [V]', fontsize = 11)
plt.legend(bbox_to_anchor = (0.5, -0.2), loc = 'center', ncol = 3, fontsize = 8, frameon = False)
plt.show()
fig3.savefig('ramp.pdf', bbox_inches = 'tight')

fig4 = plt.figure();
plt.plot(t,u4,'-',color = [70/255,53/255,177/255],label ='Ve(t)')
_,PA = ctrl.forced_response(sys,t,u4,x0)
plt.plot(t,PA, '-', color = [62/255,123/255,39/255], label ='(Vs)'  )
_,VPID = ctrl.forced_response(sysPID,t,u4,x0)
plt.plot(t,VPID, ':', linewidth = 2, color = [255/255, 116/255, 139/255], label ='VPID(t)'  )
plt.xlim(-0.25,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(-1,1); plt.yticks(np.arange(-1,1.1,0.2))
plt.xlabel('t [s]', fontsize = 11)
plt.ylabel('Vi(t) [V]', fontsize = 11)
plt.legend(bbox_to_anchor = (0.5, -0.2), loc = 'center', ncol = 3, fontsize = 8, frameon = False)
plt.show()
fig4.savefig('sine.pdf', bbox_inches = 'tight')