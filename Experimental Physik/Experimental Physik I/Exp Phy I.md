
## Kinematik

1. Reibungskraft:
$$
F_{R}  =  -\mu F_{\perp} \frac{\vec{v}}{| \vec{v} |}
$$
2. Gleichmäßiger Beschleunigung:
$$
x(t)  = \frac{1}{2} a_{0}t^{2} + v_{0}t +x_{0}
$$
3. Maximale Wurfweite $x_{w}$:
$$
x_{w}  = \frac{|\vec{v_{0}}|^{2}}{2g} \sin(2 \varphi)
$$
$$
\begin{gather}
\varphi  =  45° \implies x_{\text{max}}  = \frac{|\vec{v_{0}}|^{2}}{2g}
\end{gather}
$$
4. Ort, Geschwindigkeit, Beschleunigung Vektor:

$$
\begin{gather}
\vec{r}  = \begin{pmatrix}
x(t) \\
y(t)
\end{pmatrix}, \frac{d\vec{r}}{dt}  = \begin{pmatrix}
\dot{x}(t) \\
\dot{y}(t)
\end{pmatrix}, \frac{d^{2}\vec{r}}{dt^{2}}  =  \begin{pmatrix}
\ddot{x}(t) \\
\ddot{y}(t)
\end{pmatrix}
\end{gather}
$$

---

## Messgenauigkeit


5. SI Einheiten:
$$
\begin{gather}
\text{s} \text{ : sekunde (second)}\\
\text{m : meter}\\
\text{kg : kilogram}\\
\text{A: ampere}\\
\text{K: kelven}\\
\text{mol : Mol}\\
\text{cd: Candela}
\end{gather}
$$
6. Messwert:
$$
\boxed{\text{Messwert} =  \text{Wert} \pm\text{stat. Fehler} \pm \text{sys. Fehler} }
$$
7. Mittelwert:
$$
\langle x \rangle  = \sum_{i  = 1}^{n}x_{i} \text{P}(x_{i})
$$
8. Kont. Mittelwert:
$$
\begin{gather}
 \langle x \rangle  = \int _{-\infty}^{\infty}xf(x) \, dx 
\end{gather}
$$
9. Kont, Varianz:
$$
V  =  \sigma^{2}  = \int_{-\infty}^{\infty}(x-\langle x \rangle)^{2}f (x)  \, dx 
$$
$$
\boxed{ \sigma \text{ : Standardabweichung}}
$$
10. Poissonverteilung:
$$
\begin{gather}
P(x)  = e^{ -\mu } \frac{\mu^{x}}{x !} , x \in \mathbb{N}_{0}\\
\boxed{\mu  = \langle x \rangle, V  = \sigma^{2}  =  \mu}
\end{gather}
$$

11. Stichproben-Mittelwert:
$$
\bar{x}  =  \frac{1}{n} \sum_{i  =  1}^{n}x_{i} 
$$
$$
\lim_{ n \to \infty } \bar{x}  =  \langle x \rangle
$$
12. Standardabweichung Einzelmessung:

$$
\begin{gather}
\sigma  =  \sqrt{ \frac{1}{n-1} \sum_{i = 1}^{n}(x_{i}-\bar{x})^{2} }
\end{gather}
$$
13. Standardabweichung des Mittelwerts:

$$
\sigma_{\bar{x}}  =  \frac{\sigma}{\sqrt{ n }}
$$
14. Fehlerfortpflanzung:

$$
\sigma^{2}_{y}  = \sum_{i=1}^{n} (\frac{ \partial y }{ \partial x_{i} })^{2}\sigma^{2}_{x_{i}} 
$$
---

## Newtonische Gesetze


15. Trägheitsgesetz:
$$\boxed{
\boxed{\frac{d\vec{v}}{dt} =  0} \implies \boxed{\sum_{i=1}^{n} \vec{F}_{i }  = 0}}
$$
16. Aktionsprinzip:

$$
\boxed{\boxed{ \vec{F}  =  m \cdot a}}
$$

17. Actio = Reatio:
$$
\boxed{\boxed{\vec{F}_{1}  = -\vec{F}_{2}}}
$$
18. Impuls:
$$
\boxed{\boxed{\vec{p}  =  m \vec{v}}}
$$
19. Rakete Geschwindigkeit:
$$
v(t)  =  -v_{\tau}^{*} \ln\left( \frac{m_{0}}{m_{0}-m(t)} \right)
$$
---

## Drehbewegung

20. Polarkoordinaten:
$$
r  =  | \vec{r} |  =  \sqrt{ r_{x}^{2}+r_{y}^{2} }, \varphi   =  \arctan\left( \frac{r_{y}}{r_{x}} \right)
$$
$$
\boxed{\vec{r}  =  \begin{pmatrix}
r_{x} \\
r_{y}
\end{pmatrix}_{(x,y)} = \begin{pmatrix}
r \cdot \cos(\varphi) \\
r \cdot \sin(\varphi)
\end{pmatrix}_{(x,y)}  =  \begin{pmatrix}
\varphi \\
r
\end{pmatrix}_{(\varphi,r)}}
$$
21. Winkelgeschwindigkeit:

$$
\boxed{ \omega  =  \frac{d\varphi}{dt}  =  \dot{\varphi}  }  
$$
22. Winkel Funktion:
$$
\varphi(t)  =  \omega t + \varphi_{0}
$$
23. Schwingungsperiode $T$:
$$
T  =  \frac{2\pi}{\omega}
$$
24. Geschwindigkeit in Dreh. Bewegung:
$$
v  =  \frac{ds}{dt}  = \frac{d(r \varphi)}{dt}  =  r \frac{d\varphi}{dt}  =  \omega r 
$$
25. Gleichförmige Kreisbewegung:
$$
\begin{gather}
\vec{v}(t)  =  r \omega \begin{pmatrix}
-\sin(\omega t) \\
\cos(\omega t)
\end{pmatrix},
\vec{a}(t)  = -r\omega^{2} \begin{pmatrix}
\cos(\omega t) \\
\sin(\omega t)
\end{pmatrix}\\
\\
\boxed{\vec{a}_{Z}  = -r \omega^{2}}
\end{gather}
$$
26. Skalarprodukt:
$$
\vec{a} \cdot \vec{b}  = \begin{pmatrix}
a_{x} \\
a_{y} \\
a_{z}
\end{pmatrix} \cdot \begin{pmatrix}
b_{x} \\
b_{y} \\
b_{z}
\end{pmatrix}  = a_{x} bx+a_{y}b_{y} +a_{z}b_{z}
$$
$$
\boxed{\vec{a} \cdot \vec{b}  =  | a | \cdot | b | \cdot \cos \vartheta}
$$
27. Kreuzprodukt:
$$
\vec{a} \times \vec{b}  = \begin{pmatrix}
a_{x} \\
a_{y} \\
a_{z}
\end{pmatrix} \times \begin{pmatrix}
b_{x} \\
b_{y} \\
b_{z}
\end{pmatrix}  = \begin{pmatrix}
a_{y}b_{z} -a_{z}b_{y} \\
a_{z}b_{x} -a_{x}b_{z} \\
a_{x}b_{y} -a_{y}b_{x}
\end{pmatrix}
$$
$$
| \vec{a} |\cdot | \vec{b} | \sin(\vartheta) \cdot \vec{e}_{\perp \vec{a},\vec{b}}
$$
28. Geschwindigkeit bei Dreh. Bewegung:
$$
\vec{v}  = \vec{\omega} \times \vec{r}
$$
29. Winkelgeschwindigkeit bei Dreh. Bewegung:
$$
\vec{\omega}  =  \frac{1}{r^{2}} (\vec{r} \times \vec{v})
$$
30. Drehimpuls (angular Momemntum):
$$
\vec{L}  =  \vec{r} \times \vec{p}
$$
$$
\underbrace{\vec{L}}_{\text{Drehimpuls}}  =  \underbrace{mr^{2}}_{\text{Trägheitsmoment}} \cdot \underbrace{\vec{\omega}}_{\text{Winkelgeschw.}}
$$
$$
\vec{L}  = I \vec{\omega}
$$
31. Trägheitsmoment ( moment of inertia):
$$
I  =  m r^{2}
$$
32. Drehmoment (Torque):
$$
\vec{D}  = \vec{r} \times \vec{F}
$$


33. Bewegungsgleichung für Drehbewegung:
$$
\boxed{ \frac{d\vec{L}}{dt}  =  \sum_{i=1}^{n} \vec{D}_{i}}
$$
34. Analog (Dreh-Normal):
$$
\boxed{
\begin{gather}
\text{Normale Bewegung:}\\
\bullet \space \space \vec{v}  = \frac{d\vec{r}}{dt} \\
\\
\bullet \space \space \vec{a}  =  \frac{d\vec{v}}{dt}\\
\\
\bullet \space \space  \vec{p}  =  m \vec{v}\\
\\
\bullet \space \space \vec{F}  = \frac{d\vec{p}}{dt}
\end{gather} 
} 
\boxed{
\begin{gather}
\text{ DrehBewegung Analog:}\\
\bullet \space \space  \vec{\omega}  =  \frac{1}{r^{2}} (\vec{r} \times \vec{v})\\
\\
\bullet \space \space \ddot{\varphi}  = \frac{d\omega}{dt}\\
\\
\bullet \space \space \vec{L}  =  I \vec{\omega} \\
\\
\\ \bullet \space \space \vec{D}  =  \vec{r} \times \vec{F}
\end{gather}
}
$$
$$
\boxed{\frac{d\vec{p}}{dt}  =  \sum_{i=1}^{n} \vec{F}_{i}}\boxed{ \frac{d\vec{L}}{dt} = \sum_{i=1}^{n} \vec{D}_{i}}
$$
35. mathematisches Pendel:
$$
\begin{gather}
\bullet \space \space  \ddot{\varphi}  =  -\frac{g}{l}\varphi \\
\bullet \space \space \omega  = \sqrt{ \frac{g}{l} }\\
\bullet \space \space T  =  2\pi \sqrt{ \frac{l}{g} }
\end{gather}
$$
---

## Arbeit und Energie


36. Arbeit:
$$
dW  =  \vec{F} \cdot d\vec{r}
$$
37. Vorzeichenkonvention von Arbeit:
$$
\text{Kräfte in der Richtung der Bewegung haben poitiv Arbeit}
$$
38. Differenz in Potentialer Energie:
$$
\Delta E_{p}  = E_{p}(B) - E_{p}(A)  = \int_{B}^{A} \vec{F}  \, d\vec{r} 
$$
39. Kinetische Energie:
$$
E_{k}  =  \frac{1}{2}m v^{2}
$$
40. Differenz in Kin. Energie:
$$
E_{k}(A)-E_{k}(B)  =  \int_{B}^{A} \vec{F} d\vec{r} 
$$
41. Rotationsenergie:
$$
E_{\omega}  = \frac{1}{2}I \omega^{2}
$$
42. Energieerhaltung:
$$
\boxed{ E  =  E_{k}+E_{p}  =  \text{ constant}}
$$
43. Leistung:
$$
P  =  \frac{dW}{dt}
$$
44. Intensität:
$$
I  =  \frac{E}{\Delta t \Delta A}
$$
---

## Erhaltungssätze

45. Energie Erhaltung:
$$
\boxed{E = \sum_{i=1}^{n} E_{i}, \frac{d}{dt} E  = 0}
$$
$$
\boxed{ E  = \sum_{i=1}^{n} E_{i}  = \text{Constant}}
$$

46. Impuls Erhaltung:
$$
\boxed{\frac{d\vec{p}}{dt}  =  \sum_{i=1}^{n} F_{i}, F_{i, \forall i} = 0 \implies \frac{d\vec{p}}{dt}  = 0}
$$
$$
\boxed{\vec{P}  = \sum_{i=1}^{n} p_{i}  =  \text{ Constant} }
$$

47. Drehimpuls Erhaltung:
$$
\boxed{\frac{d\vec{L}}{dt} = \sum_{i=1}^{n} D_{i}, D_{i,\forall i}  = 0 \implies \frac{d\vec{L}}{dt} = 0}
$$
$$
\boxed{\vec{L} = \sum_{i=1}^{n} \vec{L}_{i}}
$$

---

## Stoßprozesse

48. Allgemeine elastischer Stoß Gleichung: 
$$
\begin{gather}
\vec{p_{1}} + \underbrace{\vec{p_{2}}}_{  =  0}  =  \vec{p_{1}}^{\prime} +\vec{p_{2}}^{\prime}\\
E_{1}  =  E_{1}^{\prime}+E_{2}^{\prime}
\end{gather}
$$
49. Thaleskreis Gleichung für Stoßprozesse:
$$
\begin{gather}
(p_{2x}^{\prime} -\mu v_{1})^{2}+(p_{2y}^{\prime})^{2}  = (\mu v_{1})^{2}\\
\\
\boxed{\mu \equiv \frac{m_{1}m_{2}}{m_{1}+m_{2}}}
\end{gather}
$$
50. Zentral-Stoß:
$$
\vec{p_{1}}^{\prime}  = m_{1}\left( 1-\frac{2m_{2}}{m_{1}+m_{2}} \right)v_{1}
$$
51. inelastischer Stoß:
$$
v_{1}^{\prime}  =  \left( \frac{m_{1}}{m_{1}+m_{2}} \right)v_{1}
$$

## Koordinatensysteme

52. Kartesische Koordinaten $(x,y,z)$:
$$
\begin{gather}
\vec{O}  = \begin{pmatrix}
o_{x} \\
o_{y} \\
o_{z}
\end{pmatrix}\\
\\
d\vec{s}  = \vec{e_{x}} dx + \vec{e_{y}} dy + \vec{e_{z}} dz\\
\frac{d\vec{s}}{dt}  = \vec{v}, \space \space \frac{d\vec{v}}{dt}  = \vec{a}
\end{gather}
$$
53. Zylindrische Koordinaten $(r,\varphi,z)$:
$$
\begin{gather}

\vec{O}  = \begin{pmatrix}
r \cos(\varphi) \\
r \sin(\varphi) \\
z
\end{pmatrix}\\
\\
d\vec{s}  = \vec{e_{r}} \space dr + \vec{e_{\varphi}} \space r  \space  d\varphi + \vec{e_{z}} \space  dz\\
\frac{d\vec{s}}{dt}  = \vec{v}, \space \space \frac{d\vec{v}}{dt}  = \vec{a}\\
\\
\boxed{dV  =  r \cdot\space dr \space  d\varphi \space dz}
\\
\boxed{dA  =  r  \cdot \space   dr \space  d\varphi}
\end{gather}
$$
54. Kugelkoordinaten(sphärische Koordinaten) $(r,\varphi, \vartheta)$:
$$
\begin{gather}
\vec{O}  = \begin{pmatrix}
r \cos(\varphi) \sin(\vartheta)\\
r \sin(\varphi) \sin (\vartheta)\\
r \cos(\vartheta)
\end{pmatrix}\\
\\
d\vec{s}  = \vec{e_{r}} \space dr + \vec{e_{\varphi}} \space r \sin (\vartheta) \space  d\varphi + \vec{e_{\vartheta}} \space \sin(\vartheta) \space  d\vartheta\\
\frac{d\vec{s}}{dt}  = \vec{v}, \space \space \frac{d\vec{v}}{dt}  = \vec{a}\\
\\
\boxed{dV  =  r^{2} \sin(\vartheta) \cdot\space dr \space  d\varphi \space d\vartheta}
\\
\boxed{dA  =  r^{2}\sin(\vartheta) \cdot \space   d\varphi \space  d\vartheta}
\end{gather}
$$

55. Gradient $\nabla$ von Koordinaten:
$$
\begin{gather}
\text{ Kartestisch:}\\
\nabla = \vec{e}_{x} \frac{ \partial  }{ \partial x } +\vec{e}_{y} \frac{ \partial  }{ \partial y } + \vec{e}_{z} \frac{ \partial  }{ \partial z } \\
\\
\text{Zylinder:}\\
\nabla = \vec{e}_{r} \frac{ \partial  }{ \partial r } +\vec{e}_{\varphi} \frac{1}{r}  \frac{ \partial  }{ \partial \varphi } + \vec{e}_{z} \frac{ \partial  }{ \partial z } \\
\\
\text{Kugel:}\\
\nabla = \vec{e}_{r} \frac{ \partial  }{ \partial r } +\vec{e}_{\varphi} \frac{1}{r \sin (\vartheta)}  \frac{ \partial  }{ \partial \varphi } + \vec{e}_{\vartheta} \frac{1}{r} \frac{ \partial  }{ \partial \vartheta } \\
\end{gather}
$$

## Gravitation

56. Newtons Gravitationsgesetz :
$$
\vec{F}  =  -G \frac{mM}{r^{2}} \vec{e}_{r}
$$
57. Gravitationspotential $V(r)$:
$$
\begin{gather}
V(r)  =  - \frac{GM}{r}
\end{gather}
$$
58. Gradient von Gravitationspotential:
$$
\frac{\vec{F}}{m}  =  -\nabla V
$$
59. Gravitationspotenitalenergie: 
$$
 E_{\text{pot}}  = -mV  =  - \frac{GMm}{r}
$$
60. Gravitation-gesamte Energie:
$$
\begin{gather}
E  =  E_{\text{kin}} + E_{\text{pot}}\\
\\
\boxed{E  =  \underbrace{\frac{1}{2}m\dot{r}^{2}}_{E_{\text{rad}}} + \underbrace{m\bigg[ \frac{L^{2}}{2m^{2}r^{2}}-\frac{GM}{r}\bigg]}_{V_{\text{eff}}}} 
\end{gather}
$$
61. Bahnkurven Gleichungen:
$$
\begin{gather}
\boxed{r(\varphi)  = \frac{p}{1+\epsilon \cos(\varphi)}}\\
\\
\boxed{\epsilon  = \sqrt{ 1+kE }}
\\
\boxed{p \equiv \frac{L^{2}}{(GMm^{2})}} \boxed{k \equiv \frac{2mL^{2}}{(GMm^{2})^{2}}}
\end{gather}
$$
62. Bahnkurven Arten:
$$
\begin{array}{|c|c|}
\hline\space \space \space \space \space \space  &   \text{Hyperbel} &   \text{ Parabel}  &  \text{Ellipse}  & \text{ Kreis} \\
\hline \\
 E    & E>0   & E =0   & E<0  & E  = -\frac{1}{k}\\ \\
\hline \\
\epsilon^{2}   & \epsilon^{2} >1   & \epsilon^{2}  =  1  &  0<\epsilon^{2} <1  &  \epsilon^{2}  =  0
 \\ \\
\hline
\end{array}
$$
63. Gravit. Streuprozessen:
$$
\begin{gather}
\text{Hyperbel:}\\
R_{\text{min}}  = \frac{p}{1+\epsilon}\\
\\
\text{ Parabel:}\\
R_{\text{min}}  =  \frac{p}{2}\\
\\
\end{gather}
$$
64. Gravität. Bindungszustände:
$$
\begin{gather}
\text{ Ellipse:}\\
R_{\text{min/max}}  = \frac{p}{1 \pm \epsilon}\\
\\
\text{Kreis:}\\
R  =  p
\end{gather}
$$
65. Kepler-Gesetze:
$$
\begin{gather}
\boxed{1. \, \text{ Die Planeten Bewegen sich auf Ellipsen, mit Sonne im Brennpunkt}}\\
\\
\boxed{2. \, \text{ Raduisvektor überstricht in gleichen Zeiten gleichen Flächen}}\\
\\
\boxed{3. \, \text{ Quadrate der Umlauf Zeit $T_{i}$ und dritte Potenz Halbachsen $a_{i}$ sind proportional} \, T_{i}^{2} \propto a_{i}^{3}}
\end{gather}
$$


## Transformation Zwischen Bezugsystemen

66. Galileitransformationen:
$$
\boxed{\begin{gather}
\vec{r}^{\prime}  = \vec{r}-\vec{u} \cdot t\\
\vec{v}^{\prime}  = \vec{v} - \vec{u}\\
\vec{a}^{\prime}  =  \vec{a}\\
t^{\prime}  = t
\end{gather}} \boxed{\begin{gather}
\vec{r}  = \vec{r}^{\prime}+\vec{u} \cdot t\\
\vec{v}  = \vec{v}^{\prime} + \vec{u}\\
\vec{a}  =  \vec{a}^{\prime}\\
t  = t^{\prime}
\end{gather}}
$$
67. Geschwindigkeit beim Rotat. Sys:
$$
\vec{v}  =  \vec{v}^{\prime} + \underbrace{\vec{\omega} \times \vec{r}}_{\text{Rotation}}
$$
68. Beschleunigung beim Rotat. Sys:
$$
\vec{a}^{\prime}  =  \vec{a} + \underbrace{2(\vec{v}^{\prime} \times \vec{\omega})}_{ \vec{a}_{C}} + \underbrace{\vec{\omega} \times(\vec{r} \times \vec{\omega})}_{ \vec{a}_{ZF}}
$$
69. Scheinkräfte:
$$
\boxed{\begin{gather}
\text{Corioliskraft: } \space \space \vec{F}_{C}  =  2m(\vec{v}^{\prime} \times \vec{\omega})\\
\\
\text{Zentrifugalkraft: } \space \space \vec{F}_{ZF}  =  m\vec{\omega} \times(\vec{r} \times \vec{\omega})
\end{gather}}
$$
70. Lorentztransformation:
$$
\boxed{\begin{gather}
x^{\prime}  =  \gamma(x - vt)\\
y^{\prime}  = y\\
z^{\prime}  =  z\\
t^{\prime}  = \gamma\left( t-\frac{vx}{c^{2}} \right)\\

u^{\prime}= \frac{u-v}{1-\frac{uv}{c^{2}}}\\
\\
\gamma  =  \frac{1}{\sqrt{ 1-\beta^{2} }}, \beta  =   \frac{v}{c}
\end{gather}}
$$
## Spezielle Relativitätstheorie

71. Zeitdilatation :
$$
\boxed{ \Delta t  =  \gamma \Delta t^{\prime}}
$$
72. Längenkontraktion:
$$
\boxed{\Delta l  =  \frac{1}{\gamma} \Delta l^{\prime}}
$$
73. Längenmessung in Raumzeit:
$$
\begin{gather}
D^{2}  =  \begin{pmatrix}
ct & x & 0 & 0
\end{pmatrix} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix} \begin{pmatrix}
ct \\
x \\
0 \\
0
\end{pmatrix}\\
\\
\boxed{D^{2}  = (ct)^{2}-x^{2}}
\end{gather}
$$
74. Lorenztrans. als Matrix:
$$
\begin{gather}
\begin{pmatrix}
ct^{\prime} \\
x^{\prime} \\
y^{\prime} \\
z^{\prime}
\end{pmatrix}  = \begin{pmatrix}
\gamma &  -\gamma \beta & 0 & 0 \\
-\gamma \beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} \begin{pmatrix}
ct \\
x \\
 y\\
z
\end{pmatrix}
\end{gather}
$$
75. Masse-Energie:
$$
\begin{gather}
\boxed{ E  =  mc^{2}}
\\
\\
\boxed{m  =  \gamma m_{0}}
\end{gather}
$$
76. relativistischer Impuls:
$$
\boxed{\vec{p}  = \gamma m_{0} \vec{v}  =  \gamma\vec{p}_{0}}
$$
77. Total relativistische Energie:
$$
\begin{gather}
\boxed{ E^{2}  = (m_{0}c^{2})^{2}+(pc)^{2}}
\\
\boxed{p  =  \gamma p_{0}  =  \gamma m_{0}v}
\end{gather}
$$
78. Energie-Impuls-Raum Messung:
$$
\boxed{\mathbf{P}^{2}c^{2}  =  (m_{0}c^{2})^{2}  =  E^{2}-\vec{p}^{2}c^{2}}
$$
## Dynamik Starrer Körper

79. Massendichte:
$$
\boxed{\rho  =  \frac{dm}{dV}}
$$
80. Masse durch Volumenintegral:
$$
M  =  \int_{V} \rho  \, dV 
$$
81. Schwerpunkt integral:
$$
\boxed{ \begin{gather}
\overline{X}  = \frac{1}{M}\int \rho \,  \vec{x} \, dV  = \frac{1}{M}\int \vec{x} \, dm 
\end{gather}}
$$
82. Trägheitsmoment um $x$ :
$$
\boxed{I_{x}  = \int r_{\perp}^{2} \, dm }
$$
83. Drehimpuls um $x$ :
$$
\boxed{ \vec{L}   =  I_{x} \vec{\omega}}
$$
84. Satz von Steiner:
$$
\boxed{ \mathbf{I}_{\mathcal{X}}  =  \mathbf{I}_{\overline{X}} +Ma^{2}} 
$$
$$
\boxed{ a  = | \overline{X}-\mathcal{X} |}
$$
85. Drehschwingungen gleichungen:
$$
\begin{gather}
\boxed{ D  =  -D_{r} \Phi}\\
\\
\boxed{\ddot{\Phi}  = \underbrace{-\frac{D_{r}}{I} \Phi}_{ \omega^{2}}}\\
\\
\boxed{\Phi(t)  =  A \cdot \cos(\omega t+\varphi_{0})}
\end{gather}
$$
86. Drehschwingungen Periode:
$$
\boxed{ T  =  2\pi \sqrt{ \frac{I}{D_{r}} }}
$$
87. Rotationsenergie:
$$
\boxed{ E_{\circlearrowleft}  = \frac{1}{2} \,  I \,  \omega^{2}}
$$
88. Trägheitsmoment durch Trähgheitstensor $\hat{I}$:
$$
\begin{gather}
\vec{L}  =  \hat{I} \cdot \vec{\omega}\\
\\
\begin{pmatrix}
L_{x} \\
L_{y} \\
L_{z}
\end{pmatrix}  = \begin{pmatrix}
I_{x}  & 0 & 0 \\
0 & I_{y}  & 0 \\
0 & 0 & I_{z}
\end{pmatrix} \begin{pmatrix}
\omega_{x} \\
\omega_{y} \\
\omega_{z}
\end{pmatrix}\\
\\
\boxed{ E_{\circlearrowleft}  = \frac{1}{2} \,  \vec{\omega}^{T} \,  \hat{I} \,  \vec{\omega}}\\
\\
\boxed{E_{\circlearrowleft}  =  \frac{1}{2} \vec{\omega} \cdot \vec{L}}\\
\\
E_{\circlearrowleft} = \frac{1}{2}(I_{x}\omega_{x}^{2} + I_{y}\omega_{y}^{2} +I_{z}\omega_{z}^{2})
\end{gather}
$$


89. Kreisel präzession winkelgeschwidigkeit:
$$
\boxed{ \omega_{p}  =  \frac{D}{L}} 
$$
90. Periode von Kreisel mit präzession:
$$
T_{p}  =  \frac{4\pi^{2} I_{R}}{mgr T_{R}}
$$
91. Translation vs. Rotation:
$$
\begin{array}{|c|c|} \hline \\
\text{Translation}  & \text{Symbol}  & \text{Symbol} & \text{Rotation} \\
\hline \\
\text{Verschiebung} & x & \varphi & \text{Winkel} \\
\hline \\
\text{Geschwindigkeit} & v  = \frac{dx}{dt}  & \omega  =  \frac{d\varphi}{dt} & \text{ Winkelgesch.}\\
\hline \\
\text{Beschleunigung} &a  =  \frac{dv}{dt}  & \dot{\omega}  = \frac{d\omega}{dt}  & \text{ Winkelbesch.}\\
\hline \\
\text{Masse} & m & I  =  \int r_{\perp}^{2} dm & \text{ Trägheitsmoment}\\
\hline \\
\text{Impuls} & \vec{p}  =  m\vec{v} & \vec{L}  = I \,  \vec{\omega} & \text{Drehimpuls}\\
\hline \\
\text{Kraft} & \vec{F}  =  m\vec{a}  & \vec{D}  =  \vec{r} \times \vec{F} & \text{Drehmoment}\\
\hline \\
\text{Arbeit} & W  = \int \vec{F} d\vec{r}  & W  = \int \vec{D}\vec{\omega} dt & \text{Arbeit}\\
\hline \\
\text{Kinetische Energie} & E_{\text{kin}}  =  \frac{1}{2}mv^{2}  & E_{\circlearrowleft}  =  \frac{1}{2} I \,  \omega^{2}  & \text{ Rotationsenergie}\\
\hline \\
\text{Leistung} & P  =  \vec{F} \vec{v}  & P  =  \vec{D} \vec{\omega} & \text{Leistung} \\
\hline
\end{array}
$$
92. Rotations verbindende Gleichungen:
$$
\begin{array}{|c|c|}
\hline \\ 
\text{Ziel} & \longleftarrow & \text{Variabel}\\
\hline\\
\text{Geschwindigkeit}  & \vec{v}  =  \vec{\omega} \times \vec{r} & \text{Winkelgesch.} \\
\hline \\
\text{Tangential-Beschleunigung} & \vec{a}_{t}  =  \vec{\dot{\omega}} \times \vec{r}  & \text{ Winkelbesch.}\\
\hline \\
\text{Radial-Beschleunigung} & \vec{a}_{r}  = \vec{\omega} \times \vec{v} & \text{ Winkelgesch.}\\
\hline \\
\text{Zentrifugal-Beschleunigung} & \vec{a}_{ZF}  =  \vec{\omega} \times(\vec{r} \times\vec{\omega})& \text{ Winkelgesch.}\\
\hline \\
\text{Coriolis-Beschleunigung} & \vec{a}_{C}  = 2(\vec{v}^{\prime} \times \vec{\omega})  & \text{ Winkelgesch.}\\
\hline \\
\text{Drehmoment} & \vec{D}  =  \vec{r} \times \vec{F} & \text{Kraft}\\
\hline \\
\text{Drehimpuls} & \vec{L}  =  \vec{r} \times \vec{p} & \text{ Impuls} \\
\hline
\end{array}
$$

## Schwingungen

93. Model des harmonischen Oszillators:
$$
\boxed{ \ddot{x}  =  -\omega_{0}^{2}x}
$$
$$
\begin{gather}
\boxed{ \ddot{x} + \omega_{0}^{2}x  =  0}\\
\\
\boxed{ \omega_{0}  =  \sqrt{ \frac{k}{m} } :\text{ Federkonstant}}\\
\\
\boxed{x(t)  =  x_{0} \cos(\omega_{0} \,  t + \varphi_{0})}\\
\boxed{\text{Anfangbedingungen: } x_{0} , \varphi_{0}}
\end{gather}
$$
94. Komplexe Darstellung von Wellen:
$$
\begin{gather}
\boxed{e^{ i(\omega \,  t+ \varphi_{0}) }  =  \cos(\omega  \, t + \varphi_{0}) + i \sin(\omega \,  t + \varphi_{0})}\\
\end{gather}
$$
95. Gedämpfter Oszillator:
$$
\boxed{\ddot{\Phi }+2 \gamma \dot{\Phi} + \omega_{0}^{2}\Phi  =  0}
$$
$$
\boxed{ \Phi(t)  =  \Phi_{0} \,  \cdot e^{ -\gamma \, t } \cdot \cos(\omega \, t + \varphi_{0})}
$$
$$
\boxed{\omega^{2}  =  \omega_{0}^{2}-\gamma^{2}}
$$
96. Gedämpfte Oszillator Arten:
$$
\begin{array}{|c|c|}
\hline \text{ Ungdämpfte Schwingung} & \gamma  = 0, \omega  =  \omega_{0}  & \Phi_{0} \cos(\omega_{0} \, t + \varphi_{0})\\ \hline \text{Gedämpfte Schwingung}  & \omega_{0}>\gamma, \,  \omega  = \sqrt{ \omega_{0}^{2}-\gamma^{2} }<\omega_{0}  & \Phi_{0} \, e^{ -\gamma t }\,  \cos(\omega \,  t +\varphi_{0}) \\
\hline \text{Kreichfall} & \gamma\geq \omega_{0}, \, \omega^{2} \leq 0 & \Phi_{0} \,  e^{ -\gamma t } \, \sinh(t \cdot\sqrt{ \gamma^{2}-\omega_{0}^{2} }) \\
\hline \text{Aperiodischer Grenzfall}  &  \omega  =  0 , \gamma  =  \omega_{0}  & \Phi_{0} \,  e^{ -\gamma t } \cdot t  \\
\hline
\end{array}
$$

97. Erzwungene Schwingungen:
$$
\boxed{ \ddot{\Phi} + 2 \gamma \dot{\Phi} + \omega_{0}^{2}\Phi  = \kappa e^{ i \omega_{m}t }}
$$
$$
\boxed{ \Phi(t)  =  \mathcal{C} \cdot e^{ i\omega_{m}t }}
$$
$$
\boxed{ \mathcal{C}  = \kappa \bigg[  \frac{(\omega_{0}^{2}-\omega_{m}^{2})}{ (\omega_{0}^{2}-\omega_{m}^{2})^{2} + (2\gamma \omega_{m})^{2}} - i \,  \frac{2\gamma \omega_{m}}{(\omega_{0}^{2}-\omega_{m}^{2})^{2} + (2\gamma \omega_{m})^{2}}\bigg]}
$$
98. Resonanz bei erz. Schwingungen:
$$
\Phi(t)  = \mathcal{C} \cdot e^{ i \omega_{m}  t } 
$$
$$
| \mathcal{C} |  = \kappa \bigg[ \frac{1}{ \sqrt{ (\omega_{0}^{2}-\omega_{m}^{2})^{2} + (2\gamma \omega_{m})^{2} }} \bigg]
$$
$$
\begin{gather}
\boxed{\omega_{R}  =  \sqrt{ \omega_{0}^{2}-2\gamma^{2} }}
\end{gather}
$$
99. Gekoppelte Schwingugnen:

$$
\begin{gather}
\boxed{ \Phi_{1}  = \xi^{+ } + \xi^{-}  =  2 \Phi_{0} \cos  \bigg(\frac{\omega_{1} - \omega_{2}}{2}t + \frac{\varphi_{1}-\varphi_{2}}{2} \bigg )  \cdot \cos \bigg(\frac{\omega_{1} + \omega_{2}}{2}t + \frac{\varphi_{1}+\varphi_{2}}{2}\bigg ) }\\
\\
\boxed{ \Phi_{2}  = \xi^{+ } -\xi^{-}  = —2 \Phi_{0} \sin  \bigg(\frac{\omega_{1} - \omega_{2}}{2}t + \frac{\varphi_{1}-\varphi_{2}}{2} \bigg ) \cdot \sin \bigg(\frac{\omega_{1} + \omega_{2}}{2}t + \frac{\varphi_{1}+\varphi_{2}}{2}\bigg ) }
\end{gather}
$$

100. Fourier-transform:
$$
\begin{gather}
F( \omega)  =  \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} f(t) e^{ -i \omega t } dt\\
f( t)  =  \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} F(\omega) e^{ +i \omega t } d\omega\\
\end{gather}
$$
101. Unschärferelation:
$$
\Delta \omega \cdot \Delta t \geq 1
$$

## Wellen

102. Ebene Harmonische Welle:
$$\boxed{
\underbrace{\xi(x,t)}_{\text{Auslenkung}}  =  \underbrace{\xi_{0}}_{\text{Amplitutde}}  \cdot \sin \bigg( \underbrace{k}_{\text{Wellenzahl} } \cdot \underbrace{(x-vt)}_{\text{Ausbreitung}} \bigg) }
$$
103. Wellen Variablen und ihre Relationen:
$$
\begin{array}{|c|c|}
\hline \text{Wellenzahl}  & k & \frac{2\pi}{\lambda} &  \text{Wellenlänge} \\
\hline \text{Frequenz} & f & \frac{1}{T} & \text{ Periode}\\ 
\hline \text{Kreisfrequenz} & \omega & \frac{2\pi}{f}  & \text{ Freuenz} \\
\hline \text{Phasengesch.} & v &  \frac{\omega}{k}  & \text{Wellenzahl} \\
\hline \text{Wellenlänge} & \lambda  & \frac{v}{f} & \text{Frequenz} \\
\hline
\end{array}
$$
104. Haromonische Welle in Komplexer zahlen:
$$
\boxed{\xi(x,t)  = \xi_{0} e^{ i(kx-\omega t) }}
$$
105. Wellenzahlvektor $\vec{k}$:
$$
| \vec{k} |  =  \frac{2\pi}{\lambda}
$$
$$
\vec{k} \cdot \vec{r}  = \text{ const.}
$$
106. Vektor-Ebenewelle:
$$
\begin{gather}
\boxed{ \vec{\xi}  =  \vec{\xi}_{0} \sin (\vec{k}\cdot \vec{r} -\omega t)}\\
\boxed{\vec{\xi}  =  \vec{\xi_{0}} e^{ i(\vec{k}\cdot \vec{r} -\omega t) }}
\end{gather}
$$
107. Intensität und Amplitude:
$$
\boxed{ I \propto | \xi_{0} |^{2}}
$$
108. Kugelwellen:
$$
\begin{gather}
\boxed{ \xi  =  \frac{\xi_{0}}{r} \sin(kr-\omega t)}\\
\\
\boxed{\xi  = \frac{\xi_{0}}{r}e^{ i(kr-\omega t) }}\\
\\
\boxed{ I \propto r^{-2}}
\end{gather}
$$
109. Stehende Welle:
$$
\begin{array}{|c|c|}
\hline \xi_{1}  &  =  &  \xi_{0}\sin(kx+\omega t) \\
\hline \xi_{2}  &  =  & \xi_{0}\sin(kx-\omega t+\varphi) \\
\hline \xi_{1}+\xi_{2} &  =   & 2\xi_{0} \cdot \underbrace{\sin\left( kx+\frac{\varphi}{2}  \right)}_{\text{Amplitude}} \cdot  \underbrace{\cos\left( \omega t-\frac{\varphi}{2} \right)}_{ \text{Schwingung}}\\ \hline
\end{array}
$$
$$
\begin{array}{|c|c|}
\hline \text{Schwingung-Knoten}  & kx+\frac{\varphi}{2}  =  n\pi  &  n  =  0,1,2\dots & 0, \frac{2}{4} \lambda , \frac{4}{4} \lambda, \frac{6}{4} \lambda, \dots  \\
\hline \text{Schwingung-Bäuche}  & kx+\frac{\varphi}{2}  = \frac{2n+1}{2}  & n  = 0,1,2\dots  & \frac{1}{4} \lambda , \frac{3}{4}\lambda, \frac{5}{4}\lambda, \dots \\
\hline
\end{array}
$$

110. Schwingende Saite Eigenschwingungen:
$$
\boxed{ f_{n}  =  n \cdot\frac{v}{2L}, n  =  1,2,3,\dots}
$$
111. Überlagerung von Zwei harmonischen Wellen:
$$
\begin{array}{|c|c|}
\hline\xi_{1}  &  =  &  A \sin(k_{1}x -\omega_{1}t) \\
\hline \xi_{2}  &  =  & A \sin(k_{2}x -\omega_{2}t) \\
\hline \\
 \xi_{1} + \xi_{2} & = &     2A \cdot \sin\left( \frac{k_{1}+k_{2}}{2}x-\frac{\omega_{1}+\omega_{2}}{2}t \right) \cdot \cos\left( \frac{k_{1}-k_{2}}{2}x-\frac{\omega_{1}-\omega_{2}}{2}t \right) \\
 \\
\hline \xi_{1} \approx \xi_{2} & \implies & \omega  = \frac{\omega_{1} + \omega_{2}}{2}, k  =  \frac{k_{1}+k_{2}}{2}, \Delta k  =  \frac{k_{1}-k_{2}}{2}, \Delta \omega  = \frac{\omega_{1}-\omega_{2}}{2} \\
\hline  \\
\xi_{1}+\xi_{2}  &   =   & 2A \cdot \sin(kx-\omega t) \cdot \cos(\Delta kx-\Delta \omega t) \\
 \\
\hline
\end{array}
$$
112. Phasen- und Gruppengeschwindigkeit:
$$
\begin{array}{|c|c|}
\hline \text{ Phasengeschwindigkeit} & v_{p}  & \frac{\omega}{k} \\
\hline \text{ Gruppengeschwindigkeit}  & v_{g}  & \frac{d\omega}{dk} \\
\hline \text{ Relation 1}  & v_{g}  =  v_{p}+k \frac{dv_{p}}{dk} & k, \frac{dv_{p}}{dt} \\
\hline \text{ Relation 2}  & v_{g}  = v_{p} - \lambda \frac{ dv_{p}}{d\lambda}  & \lambda, \frac{dv_{p}}{d\lambda} \\
\hline 
\end{array}
$$
113. Arten von Dispersion:
$$
\begin{array}{|c|c|}
\hline \text{ Normale Dispersion}  & \frac{dv_{p}}{d\lambda} >0 & v_{g} < v_{p} & \text{häufigster Fall} \\
\hline \text{ Keine Dispersion}  & \frac{dv_{p}}{d\lambda}  = 0 & v_{g}  =  v_{p}  & \text{Signalform erhalten} \\
\hline \text{ Anomale Dispersion}  & \frac{dv_{p}}{d \lambda} <0 & v_{g} >v_{p}  & \text{ Selten} \\
\hline
\end{array}
$$
114. Interferenz:
$$
\begin{array}{|c|c|}
\hline \xi_{1}  &   =   &  A_{1} \cdot e^{i(kr_{1}-\omega t)  }\\ 
\hline \xi_{2}  &  =  & A_{2} \cdot e^{ i(kr_{2} -\omega t) } \\
\hline \\
\xi_{1}+\xi_{2} &  =  &  e^{ i(kr_{1}-\omega t) } (A_{1}+A_{2}e^{ i \delta }) \\  
\\
\hline \text{Maxima}  &   A_{1}+A_{2}  & \delta  =  0, 2\pi, 4\pi, \dots  =  n \cdot 2\pi \\
\hline\text{Minima}  & A_{1}-A_{2} & \delta  =  \pi, 3\pi, 5\pi, \dots  =  (2n +1)\pi \\
\hline 
\end{array}
$$
115. Interferenzmuster:
$$
\begin{array}{|c|c|}
\hline \text{ Bauchlinien}  &  r_{1}-r_{2}  =  n\lambda  =  \text{const.} \\
\hline \text{Knotlinien}  & r_{1}-r_{2}  =  (2n+1) \lambda  =  \text{const.} \\
\hline
\end{array}
$$
$$
\bullet \text{ Die Kurven sind Hyperbeln}
$$
116. Dopplereffekt (Normal):
$$
\boxed{f_{B}  =  f \cdot\frac{v-v_{B} \cos(\vartheta_{B})}{v-v_{Q} \cos(\vartheta_{Q})}}
$$
117. Machsche Zahl:
$$
\begin{array}{|c|c|} \hline
\sin(\alpha)  =  \frac{v}{v_{Q}} & \text{Ma}  =  \frac{1}{\sin(\alpha)}  \\
\hline
\end{array}
$$
118. Dopplereffekt (relativistisch):
$$
\boxed{ f^{\prime}  = f \cdot \frac{\sqrt{ 1 \mp \beta }}{\sqrt{ 1 \pm \beta }}}
$$
119. Wellengleichung:
$$
\boxed{ \frac{ \partial^{2} \Psi }{ \partial x^{2} }  = \frac{1}{v^{2}}\frac{ \partial \Psi }{ \partial t }  }
$$
120. Transversale Wellen:
$$
\boxed{ f  =  \sqrt{ \frac{F}{\mu} }}
$$
$$
\boxed{ \mu  = \frac{dm}{dx}}
$$
## Hydromechanik

121. Druck:
$$
\boxed{p  =  \frac{F}{A}}
$$
122. Druck einer Wassersäule:
$$
\boxed{ p  =  \rho gh}
$$
123. Auftriebkraft $F_{A}$ :
$$
| \vec{F}_{A} |  =   g \cdot \rho_{\text{Fluss.}} \cdot V 
$$
124. Effektive Gewichtskraft $F^{\prime}_{G}$ :
$$
F^{\prime}_{G}  =  (\rho_{K} -\rho_{\text{Fluss}}) \cdot g \cdot V_{K}  =  \boxed{mg- \rho_{\text{Fluss}} \cdot g \cdot V_{K} }
$$
125. Physikalische Atmosphärischer Druck:
$$
\begin{gather}
1 \text{ atm}  =  101,325 \text{ Pa}\\
1 \text{ atm}  =  760 \text{ mm}\\
\end{gather}
$$
126. Boyle-Mariotte Gesetz:
$$
\boxed{ P_{1}V_{1}  =  P_{2} V_{2}}
$$
$$
\boxed{ T_{1}  =  T_{2}}
$$
127. Barometrisches Höhen-formel:
$$
\boxed{p(h)  =  p_{0} \cdot (e^{ -\rho_{0}/p_{0} })^{gh}}
$$
$$
\boxed{ \frac{\rho_{0}}{p_{0}}g  = 0.1256 \text{ km}^{-1}}
$$
128. Kontinuitätsgleichung:
$$
\boxed{ Av  =  Av^{\prime}}
$$
$$
\boxed{ \vec{j}  = \rho  \vec{v}}
$$
$$
\boxed{ \frac{ \partial \rho }{ \partial t } + \nabla \vec{j}  =  0}  
$$
129. Bernoulli-Gleichung:
$$
\boxed{P  =  \underbrace{\frac{1}{2}\rho v^{2}}_{\text{Staudruck}} + \underbrace{p}_{\text{Stat. Druck}} p}
$$
$$
\boxed{\frac{dP}{dt}  = 0}
$$
130. Newtonsche Reibungsgesetz:
$$
F_{R}  = \eta \cdot A \cdot \frac{dv}{dh}
$$
131. Laminar Gleichung:
$$
v(r)  =  \frac{p_{1}-p_{2}}{4 \eta l} (R^{2}-r^{2})
$$
$$
\boxed{ \text{ Parabolide Geschwindigkeitsverteilung}}
$$
132. Gesetz von Hagen-Poiseuille:
$$
\begin{gather}
J  =  \frac{V}{t}  =  \frac{\pi(p_{1}-p_{2})}{8 \eta l} R^{4}
\end{gather}
$$
133. Stationäres Gleichgewicht in Fluss.:
$$
\begin{gather}
\boxed{ \vec{F}_{R}  =  -8\pi \cdot l \cdot \eta \cdot\vec{\bar{v}}}
\end{gather}
$$
134. Kugel mit radius $r$ in einer laminaren Strömung:
$$
\boxed{ \vec{F}_{R}  =  -6\pi \cdot r \cdot \eta \cdot \vec{v}}
$$
135. Turbulent Strömungswiderstand:
$$
\boxed{ F_{W}  =  c_{W} \cdot A \frac{1}{2} \rho \, v^{2}}
$$
136. Zuspannung $\sigma$ durch Hookeschen Gesetz:
$$
\sigma  =  E \cdot \epsilon  =  E \cdot \frac{\Delta l}{l}
$$
$$
\boxed{ E : \text{ Elastizitätsmodul}}
$$
137. Elastische Voumenänderung unter Druck $p$ :
$$
p  =  K  \cdot \frac{\Delta V}{V}
$$
$$
\boxed{ K: \text{ Kompressionsmodul}}
$$
138. Schallgeschwindigkeiten in Festkörpern und Flüssigkeiten:
$$
\begin{array}{|c|c|}
\hline \text{ Festkörper} & v  =  \sqrt{  \frac{E}{\rho} } \\
\hline \text{ Flüssigkeit} & v  =  \sqrt{  \frac{K}{\rho} } \\
\hline
\end{array}
$$
$$
\begin{array}{|c|c|}
\hline \text{Gasen}  & < & \text{Flüssigketien} & < & \text{ Festkörper}\\
\hline
\end{array}
$$
139. Adiabatenkoeffizienten $\kappa$  und Gasenschallgeschwindigkeit:
$$
\begin{gather}
p_{1} V_{1}^{\kappa }  =  p_{2} V_{2}^{\kappa}\\
\\
\boxed{ v  =  \sqrt{  \frac{p \cdot\kappa}{\rho} }}
\end{gather}
$$

