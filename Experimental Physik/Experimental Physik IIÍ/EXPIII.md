
## Misc

1. Spektrum Sichtbares Lichtes:
$$
380 \times 10^{-9} \text{ m}<\lambda < 780 \times 10^{-9} \text{ m}
$$


---

## Wellen_Vakuum


2. Mxuell-Gleichungen:
$$
\boxed{\begin{gather}
\nabla \times \vec{E}  =  - \frac{ \partial \vec{B} }{ \partial t } \\
\nabla \cdot \vec{B}  =  0\\
\\
\nabla \cdot \vec{D}  =  \rho
\\
\nabla \times \vec{H}  =  \vec{j} + \frac{ \partial \vec{D} }{ \partial t } \\
\end{gather}  } \space \space \boxed{\begin{gather}
\vec{D}  =  \epsilon_{0} \epsilon_{r} \vec{E}\\
\vec{H}  =  \frac{1}{\mu_{0}\mu_{r}} \vec{B}\\
\vec{j}  =  \sigma \vec{E}
\end{gather}}
$$
$$
\begin{gather}
\epsilon_{0}  = \frac{1}{\mu_{0}c_{0}^{2}}  = 8.85 \text{ F/m : Dielktrizitätskonz.}\\
\epsilon_{r}: \text{ relative Dielktrizitätskonz.}\\
\mu_{0}  = 4 \pi \times 10^{-7} \text{ N/A$^{2}$ : Permeabilitätskonz.}\\
\mu_{r} : \text{ relative Permeabilitätskonz.}\\
\vec{j} : \text{ Stormdichte}\\
\sigma: \text{ Leitfähigkeit}
\end{gather}
$$
3. Ebene Elektrische Wellen:
$$
\begin{gather}
\vec{E} (z,t)  = 2\vec{A}_{0} \cos(kz - \omega t )\\
E_{x}(z,t)  = E_{0,x} \sin(kz -\omega t + \varphi_{x})\\
E_{y}(z,t)  = E_{0,y} \sin(kz -\omega t + \varphi_{y})
\end{gather} 
$$

4. Linear Polarisation:
$$
\begin{gather}
\boxed{ \varphi_{x}  =  \varphi_{y}}\\
E_{x}(z,t)  =  E_{0,x} \sin(kz- \omega t)\\
E_{y}(z,t)  = E_{y,0} \sin(kz - \omega t)\\
\\
E_{x}(z,t)  = E_{0} \sin(kz - \omega t) \text{  koordinatenwechsel}\\
\vec{B}  =  \frac{1}{\omega}(\vec{k} \times \vec{E})\\
| \vec{B} |  =  \frac{1}{c} | \vec{E} |
\end{gather}
$$
5. Zirkular Polarisation:
$$
\begin{gather}
\boxed{ \varphi _{x}  =  \varphi_{y} \pm \frac{\pi}{2}}\\
E_{x}(z,t)  = E_{0,x} \cos(kz -\omega t )\\
E_{y}(z,t)  = \pm E_{0,y} \sin(kz -\omega t )\\
\\
\boxed{ \sigma^{+} \text{ rechts zirkular}}\\
\boxed{\sigma^{-} \space \space \text{ links zirkular}}
\end{gather}
$$


6. Energie ElektroMag. Wellen/ Poynting Vektor:
$$
\begin{gather}
I  = c \epsilon_{0}E^{2} \text{ (konz. beim zirkular pol. Licht)}\\
\langle I(t) \rangle  =  \frac{1}{2}c\epsilon_{0} E_{0}^{2}\\
\\
\vec{S}  =  (\vec{E}\times \vec{H})\\
\end{gather}
$$
7. Strahlendruck und impuls:
$$
P  =  \frac{I}{c}
$$
$$
p  =  I /c^{2}
$$
---

## Brechung

8. Brechungsindex:
$$
\begin{gather}
c_{ \text{Materie}}(\lambda)  = \frac{c_{0}}{n(\lambda)}\\
\\
\boxed{n>1 \text{ : Brechungsindex (wirkung: dispersion)}}\\
\boxed{\omega,f \text{ bleiben gleich!}}
\end{gather}
$$

9. Zusätzliche Zeit nach Laufen in Materie:
$$
\begin{gather}
\Delta t  =  \frac{\Delta z}{c_{0}}(n -1)\\
\end{gather}
$$

10. Wellengleichung nach Laufen in Materie:
$$
\vec{E}(z,t)  =  \vec{E}_{0} \cdot e^{ i(\omega t  -kz) } \cdot e^{ -i\omega(\Delta t) }
$$

11. Maxuell-Beziehung bei nicht ferromagnetische $\boxed{\mu_{r} \approx 1}$ Medien:
$$
n  =  \sqrt{ \epsilon_{r} }
$$
12.  Brechungsindex abhä. von dipol $N$ und Polarisierbarkeit $\alpha$:
$$
\begin{gather}
n^{2}  =  1 + \frac{\alpha N}{\epsilon_{0}}
\end{gather}
$$
13. Brechungsindex als Komplexe Zahl:
$$
\boxed{ \begin{gather}
\boxed{n^{2}  = 1+\frac{N\alpha}{\epsilon_{0}}  = 1+ \frac{e^{2}N}{\epsilon_{0}m}\cdot \bigg[ \frac{\omega_{0}^{2}-\omega^{2}}{(\omega_{0}^{2}-\omega^{2})^{2}+(\gamma \omega)^{2} }- i \frac{\gamma \omega}{(\omega_{0}^{2}-\omega^{2})^{2}+(\gamma \omega)^{2}} \bigg]}\\
\end{gather}}
$$
$$
\begin{array}{|c|c|}
\hline N & \text{ Dipol Nummer} \\
\hline e & \text{Elektron } \\
\hline m & \text{Elektron masse}  \\
\hline \alpha  &  \text{Polarisierbarkeit} \\
\hline 
\end{array}
$$

14. Beer’sches Absorptionsgesetz :
$$
\begin{gather}
I = I_{0} \cdot e^{ -\alpha z }\\ \\
\alpha =  \frac{4\pi \kappa}{\lambda} = 2k_{0} \kappa \\
\alpha: \text{ Absorptionskoeffizent}\\\\
\delta = \frac{1}{\alpha} \space \space \text{ , nach jede $\delta$ } \to \left( \times \frac{1}{e} \right)\\
\delta : \text{ Eindrigtiefe}
\end{gather}
$$
15. Reelle und imaginäre Teile von Brechnung :
$$
\begin{array}{|c|c|}
\hline \text{Dispersionsrelation}  &  & n  =  n_{r} -i\kappa \\
\hline n_{r}   &  =  & 1+ \frac{Ne^{2}}{2\epsilon_{0}m}\cdot \frac{\omega_{0}^{2}-\omega^{2}}{(\omega_{0}^{2}-\omega^{2})^{2}+(\gamma \omega)^{2}} \\
\hline \kappa  &  =  & \frac{Ne^{2}}{2\epsilon_{0}m}\cdot \frac{\gamma \omega}{(\omega_{0}^{2}-\omega^{2})^{2}+(\gamma \omega)^{2}} \\
\hline
\end{array}
$$
16. Reelle Brechungsindex bei nicht magnet. medien:
$$
n_{r}  =  \sqrt{ \epsilon }
$$
$$
\boxed{ \epsilon \text{ ist Dielektrizitätskonstante}}
$$
17. Phasen und Gruppen Geschwindigkeit:
$$
\begin{array}{|c|c|}
\hline \text{Phasen Gesch.}  & \frac{\omega}{k}  =  c  =  \frac{c_{0}}{n_{r}} \\
\hline \text{ Gruppen Gesch.}  & \frac{ \partial \omega }{ \partial k }   = \frac{c_{0}}{n_{r} +\omega \frac{ \partial n_{r} }{ \partial \omega } } \\
\hline \frac{ \partial n_{r} }{ \partial \omega }  & \frac{Ne^{2}}{2\epsilon_{0}m} \cdot \frac{2\omega ((\omega_{0}^{2}-\omega^{2})^{2}-(\gamma \omega)^{2})}{((\omega_{0}^{2}-\omega^{2})^{2}+ (\gamma \omega)^{2})^{2}} \\
\hline
\end{array}
$$
18. Normale vs. Anormale Dispersion:
$$
\begin{array}{|c|c|}
\hline \text{ Normale Dispersion} & \frac{ \partial n_{r} }{ \partial \omega } >0 & v_{gr} <c  =  v_{ph} \\
\hline \text{ Anomale Dispersion}  & \frac{ \partial n_{r} }{ \partial \omega } <0 & v_{gr} >c = v_{ph} \\
\hline \\
\text{Anomale Disp. Bereich} & \omega_{0}-\frac{\gamma}{2} <\omega < \omega_{0}+\frac{\gamma}{2}  & v_{gr} >c_{0} \\
 \\
\hline
\end{array}
$$

19. Brechungsindex in Leitfähigen Medium:
$$
\begin{gather}
n  =  \sqrt{ \epsilon_{r} - i \frac{\sigma}{\omega\epsilon_{0}}}\\
\\
n_{r}^{2}-\kappa^{2}  = \epsilon_{r} \\
2n_{r} \kappa  =  \frac{\sigma}{\epsilon_{0}\omega}
\end{gather}
$$

20. Allgemein brech. gleichung für leit. medien mit plasmafrequenz:
$$
\begin{array}{|c|c|}
\hline n^{2}  &  =  & 1- \frac{e^{2}N}{\epsilon_{0}m (\omega^{2} -i \gamma \omega)} \\
\hline \omega_{p}  &  =   & \sqrt{ \frac{Ne^{2}}{\epsilon_{0}m} } \\
\hline n^{2}   &  =   & 1-\frac{\omega_{p}^{2}}{\omega^{2}-i\gamma \omega}  \\
\hline
\end{array}
$$
21. Streuzeit be leitfähigen med.:
$$
\tau  =  \frac{1}{\gamma}
$$
22. Grenzfälle für Leitfähigen med. :
$$
\begin{array}{|c|c|}
\hline n^{2}   &  =  & 1- \frac{\omega_{p}^{2}}{\omega^{2}\left( 1-\frac{i}{\omega \tau} \right)} \\
\hline \text{ Niedrige Freq.}  & \omega \tau \ll 1 \ll \omega_{p}\tau  & n_{r}  =  \kappa  =  \sqrt{ \tau \frac{\omega_{p}^{2}}{2\omega} } \\
\hline \text{ Hohe Freq.}  &  1 \ll \omega \tau < \omega_{p} \tau & n_{r}  =  0, \kappa  = \sqrt{ \frac{\omega_{p}^{2}}{\omega^{2}}-1 } \\
\hline \text{Höhre Freq.} & 1 \ll \omega_{p} \tau < \omega \tau  & \kappa  = 0, \text{ (durchsichtig!)} \\
\hline
\end{array}
$$

## Reflexion_Transmission

23. Snelliussches Brechungsgesetz:
$$
\boxed{ \alpha  =  \alpha ^{\prime} \text{: Reflexionsgesetz}}
$$
$$
\boxed{ n_{1} \sin \alpha  =  n_{2} \sin \beta \text{ : Snell. Brechungsgesetz}}
$$
24. Totalreflexion winkel:
$$
\boxed{\sin \alpha  =  \frac{n_{2}}{n_{1}}}
$$
25.  Fresnel-Formeln:
$$
\begin{array}{|c|c|}
\hline \text{ Senkrecht} & \text{ Parallel} \\
\hline\rho_{s}  = -\frac{\sin(\alpha-\beta)}{\sin(\alpha+\beta)}  &  \rho_{p}  =  -\frac{\tan(\alpha-\beta)}{\tan(\alpha+\beta)}\\
\hline \tau_{s}  =  2 \frac{\cos \alpha \sin \beta}{\sin (\alpha+\beta)}  & \tau_{p}  =  2 \frac{\cos \alpha \sin \beta}{\sin(\alpha+\beta)\cos(\alpha-\beta)} \\
\hline  
\end{array}
$$
26. Reflexions- und Transmissionsvermögen:
$$
\begin{gather}
\boxed{ R_{s}  =  \left( \frac{\sin(\alpha-\beta)}{\sin(\alpha+\beta)} \right)^{2} , T_{s}  =  1- R_{s}}\\
\boxed{R_{p}  =  \left( \frac{\tan(\alpha-\beta)}{\tan(\alpha+\beta)} \right)^{2}, T_{p}  =  1- R_{p}}\\
\boxed{ R(\alpha  =  0)  =  \left( \frac{n_{1}-n_{2}}{n_{1}+n_{2}} \right)^{2}}
\end{gather}
$$
27. Brewster-Winkel:
$$
\boxed{ \tan \alpha_{B}  =  \frac{n_{2}}{n_{1}}}
$$
28. Reflexion an Metalloberfächen :
$$
R  =  \frac{(n_{r}-1)^{2} + \kappa^{2}}{(n_{r}+1)^{2}+\kappa^{2}}
$$


## Polarisation


29. Arten von Polarisaion:
$$
\begin{array}{|c|c|}\hline
E_{x}(z,t)  &   =   &  E_{0,x} \sin(kz-\omega t + \varphi_{x}) \\
\hline E_{y}(z,t) &   =   &  E_{0,y} \sin(kz-\omega t + \varphi_{y}) \\
\hline \text{Linear} &  & \varphi_{x}  =  \varphi_{y} \\
\hline \text{Zirkular}  &  & \varphi_{x}-\varphi_{y}  =  \pm \frac{\pi}{2} \\
\hline \text{ Elliptisch} &  & \text{sonst.} \\
\hline
\end{array}
$$
30. Malusches Gesetz:
$$
\boxed{ I ( \theta)  =  I_{0} \cos(\theta)^{2}}
$$

31. Polarisationgrad:
$$
\Pi  =  \frac{I_{\parallel}-I_{\perp}}{I_{\parallel}+I_{\perp}}
$$
32. Phasenunterschied in allgemeinenen Plätten:
$$
\Delta \varphi  =  \frac{2\pi}{\lambda_{0}} d \cdot \Delta n
$$
$$
\text{d: Dicke, $\lambda_{0}$ : Originale wellenlänge}
$$
33. $\lambda / 4$ Plättchen:
$$
d  =  \frac{\lambda_{0}}{4 \Delta n}
$$
$$
\theta  =  45^{\circ} \implies \text{ Zirkular}  \, \sigma^{-}
$$
34. $\lambda / 2$ Plättchen:
$$
\begin{gather}
d  =  \frac{\lambda_{0}}{2 \Delta n}\\
\\
\text{Spiegeln um Optiche Achse}
\end{gather}
$$
35. Phasenverschieber Null und Max:
$$
\begin{array}{|c|c|}
 \hline \text{Parallel}\\
\hline \text{ Max} & 0, 2\pi, 4\pi\dots \\ 
\hline \text{ Null } & \pi, 3 \pi, 5\pi\dots \\
\hline
\end{array}
$$
$$
\text{gekreuzt: andersrum}
$$


## Brechungsanwendungen

36. Optische Aktivität :
$$
\alpha  =  \alpha_{s} d
$$
$$
\alpha \text{: Optische drehvermögen}
$$
$$
\alpha  =  \frac{\pi}{\lambda_{0}}d(n^{-}-n^{+})
$$
$$
\begin{array}{|c|c|}
\hline +  & \text{ links zirkular} \\
\hline-  &  \text{rechts zirkular} \\
\hline
\end{array}
$$
37. Faraday Effekt:
$$
\beta  =  \nu B d
$$
$$
\nu\text{: Konstant}, d: \text{dicke}, B:\text{ magnetisches Feld} 
$$
38. Kerr Effekt:
$$
\Delta n  =  \lambda_{0} K E^{2}
$$
$$
\begin{gather}
K: \text{ Kerr konstante}
\\ E: \text{ Elektrisches Feld}
\end{gather}
$$

## Interferenz

39. Intensität von zwei wellen:

$$
\langle I \rangle  =  \langle I_{1} \rangle+\langle I_{2} \rangle + 2\sqrt{ \langle I_{1} \rangle \langle I_{2} \rangle } \cos(\Delta \varphi)
$$
$$
\boxed{ \Delta \varphi  =  (\vec{k}_{1}-\vec{k}_{2})r+ (\varphi_{1}-\varphi_{2})}
$$
$$
\begin{array}{|c|c|}
\hline\langle I_{1}  \rangle  =  \langle I_{2} \rangle  =  \langle I_{0} \rangle  & 4 \langle I_{0} \rangle \cos ^{2}\left( \frac{\Delta \varphi}{2} \right) \\
\hline \text{Konstruktive} & \Delta \varphi  = \pm 0, 2\pi,4\pi\dots \\
\hline\text{ Destrucktive } & \Delta \varphi  = \pm \pi, 3 \pi \dots
\\\hline 
\end{array}
$$

40. Interferenz von kugelwellen:
$$
\begin{array}{|c|c|}
\hline \text{ Kons. muster} & r_{1}-r_{2}  = \frac{2\pi}{k}m   =  m\lambda\\
\hline \text{ dest. muster} & r_{1}-r_{2}  =  (m+\frac{1}{2})\lambda
 \\
\hline\end{array}
$$
41. Kohärenz-Frequenzbreite:
$$
\Delta f  =  \frac{1}{\Delta t_{c}}
$$
$$
\Delta s_{c}  =  c \Delta t_{c}
$$
$$
\begin{gather}
\Delta s_{c} \text{ koh. länge}\\
\Delta t_{c} \text{ koh. zeit}
\end{gather}
$$
42. Doppelspalt maxima:
$$
y_{max}  =  \frac{s}{a} m \lambda
$$
$$
I  =  4 I_{0} \cos ^{2}\left( \pi \cdot\frac{ a}{s}\cdot \frac{y}{\lambda} \right)
$$
$$
\begin{gather}
a \text{ : Abstand zwischen spalten}\\
s \text{: Abstand von schrim}
\end{gather}
$$
43. Kohärenzfläche für dopppelspalt:
$$
F_{c}  =  \frac{\lambda^{2}}{\frac{b_{max}}{d}}  =  \frac{\lambda^{2}}{d \Omega}
$$
44. Phasen diff. in michelson interferometer:

$$
\Delta \varphi  =  \frac{2\pi}{\lambda }\Delta s
$$
$$
\langle I_{B} \rangle  =  \frac{1}{2} \langle I_{e} \rangle(1+\cos\Delta \varphi)
$$

45. Ringenzahl in michelson:
$$
\lambda  =  2 \frac{\Delta z}{N}
$$
46. Mach-zehnder interferometer:
$$
\Delta \varphi  =  \frac{2\pi}{\lambda_{0}}\Delta n \cdot L
$$
47. Dielektriche schichten, zwei:
$$
\begin{array}{|c|c|}
\hline \text{Refl. am dichteren} & \rho_{s}<0, \rho_{p}>0 & \Delta\varphi-\pi \\
\hline\text{Refl. am dünneren} & \rho_{s} >0, \rho_{p}<0 &  \Delta\varphi \\
\hline
\end{array}
$$
$$
\begin{array}{|c|c|}\hline
\Delta s &  =  & 2d \sqrt{ n_{2}^{2}-\sin ^{2}\alpha } \\
\hline \Delta \varphi &  =  &  \frac{2\pi}{\lambda } \Delta s \\
\hline\Delta \varphi^{\star}\ &  =  & \Delta \varphi-\pi  \\
\hline
\end{array}
$$
$$
\begin{array}{|c|c|}
\hline &  \text{ Dichteren} & \text{Dünneren} \\
\hline\text{Max} & 2d\sqrt{ n_{2}^{2}-\sin ^{2}\alpha }  =  \left( m+\frac{1}{2} \right)\lambda & 2d\sqrt{ n_{2}^{2}-\sin ^{2}\alpha }  =  m\lambda \\
\hline
\end{array}
$$

48. Airy-Formeln für vielstrahl interferenz:
$$
\begin{array}{|c|c|}
\hline F  &   =   &  \frac{4R}{(1-R)^{2}} \\
\hline I_{R } &  =   & I_{0} \cdot \frac{F\sin ^{2}\left( \frac{\Delta \varphi}{2} \right)}{1+F\sin ^{2}\left( \frac{\Delta \varphi}{2} \right)} \\
\hline \\
 I_{T}  &   =   & I_{0} \cdot \frac{1}{1+F\sin ^{2}\left( \frac{\Delta \varphi}{2} \right)} \\
\hline
\end{array}
$$
49. wellenlänge bestimmung durch vielstrahl interferometer:
$$
 \lambda  =  \Delta s  =  \frac{2d}{m} \sqrt{ n_{2}^{2}-\sin ^{2}\alpha }
$$
50. Fabry-perot-interferometer:

$$
\begin{array}{|c|c|} 
\hline  \text{abstand zwischen zwei wellenlängen} & \delta \lambda  =  \frac{2nd}{m(m+1)}\\
\hline \text{freier spektralbereich} & \delta f  =  \frac{c}{2nd} \\
\hline \text{Halbwertbreite}  &\Delta f  =  \frac{c}{2nd} \cdot \frac{1-R}{\pi \sqrt{ R }}\\
\hline\text{Finesse( anzahl von wellen)} & F^{*}  =  \frac{\delta f}{\Delta f}  =  \frac{\pi \sqrt{ R }}{1-R} \\
\hline 
\end{array}
$$
## Beugung

51. Einzelspalt Intensitätsverteilung:
$$
\boxed{ I(\theta)  =  I_{e} \cdot \bigg [\frac{\sin\left( \frac{\pi}{\lambda}b\sin(\theta) \right)}{\frac{\pi}{\lambda }b\sin(\theta)}\bigg]^{2}}
$$
$$
\begin{array}{|c|c|}
\hline \text{Nebenmaxima} & \sin(\theta)  =  \left( m+\frac{1}{2} \right) \frac{\lambda}{b} & \sin(\theta ) =  \frac{3}{2} \frac{\lambda}{b}, \frac{5}{2} \frac{\lambda}{b},\dots \\
\hline \text{ Nebenminima} & \sin(\theta)  =  m \frac{\lambda}{b} & \sin(\theta)  =  \frac{\lambda}{b}, 2 \frac{\lambda}{b},\dots \\
\hline -1 \text{ Nebenmin} <\theta< 1 \text{ Nebenmin}  & 2 \frac{\lambda}{b} & 90\%  \\
\hline
\end{array}
$$

52. Kreisförmige Öffnung:
$$
\boxed{ I(\theta)  =  4 I_{0} \left( \frac{J_{1}\left( \frac{2\pi r}{\lambda}\sin(\theta) \right)}{\frac{2\pi}{r} \sin(\theta)} \right)^{2}}
$$
$$
\boxed{\sin(\theta)_{\text{min,1}}  = 0.61 \frac{\lambda}{r}}
$$
53. Beugung am doppelspalt:
$$
\boxed{ I(\theta)  =  I_{e} \cdot \left( \frac{\sin\left( \frac{\pi b}{\lambda}\sin(\theta) \right)}{\frac{\pi b}{\lambda} \sin(\theta)}  \right)^{2} \cdot \left( \frac{\sin\left( 2\frac{\pi a}{\lambda}\sin(\theta) \right)}{\sin(\frac{\pi a}{\lambda} \sin(\theta))}  \right)^{2} }
$$
$$
\begin{gather}
\boxed{ a \text{:  Abstand zwischen spalten}}\\
\boxed{b \text{: Breite von Öffnungen}}
\end{gather}
$$
54. Beugung am Gitter Gleichung:
$$
\boxed{ \Delta s  =  d \sin \theta}
$$
$$
\boxed{ I(\theta)  =  I_{e} \cdot \left( \frac{\sin\left( \frac{\pi b}{\lambda}\sin(\theta) \right)}{\frac{\pi b}{\lambda} \sin(\theta)}  \right)^{2} \cdot \left( \frac{ \sin\left( N \frac{\pi d}{\lambda}\sin(\theta) \right)}{\sin(\frac{\pi d}{\lambda} \sin(\theta))}  \right)^{2} }
$$
$$
\begin{gather}
\boxed{ d \text{ : Abstand zwischen gittern}}\\
\boxed{ b \text{ : Öffnungsbreite }}
\end{gather}
$$
$$
\boxed{\text{ Hauptmaxima: } \sin(\theta)  =  m \frac{\lambda}{d}}
$$
55. Auflösungsvermögen von Gitter:
$$
\boxed{ \frac{\lambda}{\Delta \lambda}  =  Nm}
$$
56. Fresnel und Fraunhoferbeugung:
$$
\begin{array}{|c|c|}
\hline \text{ Nahzone} &  z_{0} \ll \frac{b^{2}}{\lambda}  &  \text{ Fresnelbeugung} \\
\hline \text{ Fernzone} &  z_{0}\gg \frac{b^{2}}{\lambda}  &  \text{Fraunhofer} \\
\hline
\end{array}
$$

## Geometrische_Optik

57. Lochkamera :
$$
\begin{array}{|c|c|}
\hline d^{\prime}   &  =  & \frac{a+b}{a}d \\
\hline d_{\text{beug}} &   =   & 2b \frac{\lambda}{d} \\
\hline d_{\text{Optimal}}  &   =   & \sqrt{ \frac{2ab}{a+b}\lambda } \\
\hline
\end{array}
$$
$$
\begin{array}{|c|c|}
\hline d  & : & \text{Loch durchmesser} \\
\hline d^{\prime} & : & \text{Effektive durchmesser drinnen} \\
\hline d_{\text{beug}} & : & \text{Beugungsdurchmesser} \\
\hline d_{\text{Optimal}} & : & \text{Optimale Schärfe} \\
\hline
\end{array}
$$

58. Brennweite $f$ von sphärischem Hohlspiegel:
$$
\boxed{ \frac{1}{g} +\frac{1}{b} \approx \frac{1}{f} \approx \frac{2}{R}}
$$
$$
\begin{array}{|c|c|}
\hline R & \text{ Radius} \\
\hline g  & \text{ Gegenstandweite} \\
\hline b  & \text{Bildweite} \\
\hline
\end{array}
$$
$$
\Gamma  =  -\frac{b}{g}
$$
59. Parabolspiegel:
$$
\begin{array}{|c|c|}
\hline \text{ Parabolgleichung} & y^{2}  =  4fx \\
\hline \text{ Brennweite} & f  \\
\hline
\end{array}
$$
60. Prism gleichungen:
$$
\begin{array}{|c|c|}
\hline \delta &   =   & \alpha_{1}+\alpha_{2}-\gamma  \\
\hline \frac{d\delta}{dt} &  =   & \frac{2\sin\left( \frac{\gamma}{2} \right)}{\sqrt{ 1-n^{2} \sin ^{2}\left( \frac{\gamma}{2} \right) } } \cdot \frac{dn}{d\lambda} \\
\hline n  &   =   & \frac{\sin\left( \frac{\delta+\gamma}{2} \right)}{\sin\left( \frac{\gamma}{2} \right)} \\
\hline
\end{array}
$$
61. Sphärsche Grenzfläche gleichung:
$$
\boxed{ \frac{n_{1}}{g}+\frac{n_{2}}{b}  = \frac{n_{2}-n_{1}}{r}}
$$
$$
\boxed{ \frac{n_{1}}{g}  =  \frac{n_{2}-n_{1}}{r}  = \frac{1}{f_{g}}}
$$
$$
\text{ Gegenstandbrennweite}
$$
$$
\boxed{ \frac{n_{2}}{b}  = \frac{n_{2}-n_{1}}{r}  =  \frac{1}{f_{b}}}
$$
$$
\text{ Bildbrennweite}
$$
62. Dünnen Bikonvexen Linse Gleichung (Linse maker equation):
$$
\boxed{ \frac{1}{g}+\frac{1}{b}  =  (n-1)\left( \frac{1}{r_{2}} -\frac{1}{r_{1}}  \right)  =  \frac{1}{f}}
$$
$$
\boxed{ \Gamma  =  -\frac{b}{g}  =  \frac{f}{f-g}} 
$$
63. Dicke Linse Gleichung:
$$
\boxed{ \frac{1}{f}  =  (n-1) \left( \frac{1}{r_{2}}-\frac{1}{r_{1}}+\frac{(n-1)d}{nr_{1}r_{2}} \right)}
$$
$$
\frac{1}{b}+\frac{1}{g}  =  \frac{1}{f}
$$
$$
\boxed{!} \, b,g \text{ von Hauptebenen}
$$
64. Gesamte Brennweite eines Lensensystems:
$$
\boxed{ \frac{1}{f_{r}}  =  \frac{1}{f_{1}-d} +\frac{1}{f_{2}}}
$$
$$
d\ll f_{1}+f_{2} \implies \frac{1}{f_{r} }  =  \frac{1}{f_{1}}+\frac{1}{f_{2}}
$$
$$
D  =  D_{1}+D_{2}
$$
$$
f\text{ ist von letzten Linse}
$$
65. Dioptrie Def.:
$$
D  =  \frac{1}{f}
$$
66. Chromatische Aberration:
$$
f  =  \frac{1}{n(\lambda)-1} \frac{r_{1} r_{2}}{r_{1}-r_{2}}
$$

## Anwendungen

67. Sehfehler:
$$
\begin{array}{|c|c|}
\hline \text{ Kurzsichtigkeit}  & f<A  & \text{Zerstreuung} \\
\hline \text{Weitsichtigkeit} & f>A & \text{Sammellense} \\
\hline
\end{array}
$$
68. Akkomodation:

$$
\frac{f_{1}}{g}+\frac{f_{2}}{b}  =  1
$$
$$
\text{Linse mit unterschiedliche brennweiten} f_{1},f_{2}
$$
69. Lupe:
$$
\begin{array}{|c|c|}
\hline \epsilon  & \frac{G}{f} \\
\hline \epsilon_{0} & \frac{G}{s_{0}} \\
\hline V_{\text{Lupe}} & \frac{s_{0}}{f} \\
\hline
\end{array}
$$
70. Mikroskop:
$$
\begin{array}{|c|c|}
\hline \tan \epsilon & G \frac{b}{g} \frac{1}{f_{2}} \\
\hline \tan\epsilon_{0} & \frac{G}{s_{0}}  \\
\hline V_{\text{Mikro}} & \frac{b}{g} \frac{s_{0}}{f_{2}}  & \frac{(d-f_{2})s_{0}}{f_{1}f_{2}} \\
\hline
\end{array}
$$
71. Fernohr:
$$
\boxed{ V_{\text{Fernohr}}  =  \frac{f_{Ob}}{f_{Ok}}}
$$
72. Auflösungsvermögen:
$$
\boxed{ \delta_{\text{min}}  =  1.22 \frac{\lambda}{D}}
$$
$$
\boxed{d_{\text{Beug}} = 2.4 \frac{\lambda}{D}f}
$$

$$
\boxed{ \text{D : Blende durchmesser}}
$$
$$
\boxed{ d_{\text{beug}}: \text{ durchmesser von aufgelösten Bild}}
$$
73. Auflösungsverm. Mikroskop:
$$
\boxed{ \Delta x_{\text{min}}  =  0.6 \frac{\lambda_{0}}{NA}}
$$
$$
\boxed{ NA  =  n \sin \alpha}
$$
$$
\boxed{ \alpha : \text{ Öffnungswinkel}}
$$
74. Öffnungswinkel formel:
$$
 \boxed{ \Omega  =  \frac{\pi}{4} \left(  \frac{D}{f} \right)^{2}}
$$

75. Blendenzahl:
$$
\boxed{ F  =  \frac{f}{D}}
$$
76. Kamera Gleichung:
$$
\boxed{ H  =  \Delta t \cdot\frac{\text{ISO}}{F^{2}}}
$$
$$
H: \text{ Helligkeit}
$$
$$
\text{ISO : empfindlichkeit}
$$
$$
F : \text{ Blendenzahl}
$$
77. Lichtweg in der Atmosphäre:
$$
d\varphi  =  -\frac{1}{n} \cdot \frac{dn}{dr} ds
$$
78. Refraktions Deratmosphäre:
$$
\boxed{ \rho  =  (n_{0} -1) \tan(\zeta_{s})}
$$
$$
\boxed{\rho  =  \zeta_{w}-\zeta_{s}}
$$
## Quantenphysik:

79. Photoelektriceffekt:
$$
\boxed{ e U _{\text{max}} = \hbar \omega-W}
$$
80. Energie von Photonen:
$$
\boxed{E  =  \hbar \omega  =  hf}
$$
81. Impuls von Photonen:
$$
\boxed{ \vec{P}  =  \hbar \vec{k}}
$$
82. Energie dichte schwarzkörper:

$$
\boxed{u(\nu,T)  =  \frac{8\pi h\nu^{3}}{c^{3}} \cdot \frac{1}{e^{ h\nu/kT } -1}}
$$
$$
\text{ in Polarisationsrihtung}
$$
$$
\boxed{ P(\nu,T)  =  \frac{h\nu^{3}}{c^{2}} \cdot \frac{1}{e^{ h\nu/kT }-1}}
$$
83. Wienchesverchiebungsgesetz:
$$
\boxed{\lambda_{m } =  \frac{2.88  \cdot 10^{-3}}{T} \, \text{mK}}
$$

84. Boltzmanngesetz:
$$
\boxed{ P  =  \sigma \cdot A \cdot \epsilon \cdot T^{4}}
$$
85. Compton-Effekt:
$$
\boxed{ \Delta \lambda  =  \frac{h}{m_{0}c} (1-\cos \theta)}
$$
$$
\frac{h}{m_{0}c}  =  2.42 \cdot 10 ^{-12} \text{m}
$$
86. Gitter und Elektronen Scattering:

$$
\Delta s  = 2d \sin(\alpha)
$$
$$
\alpha: \text{ Einfallswinnkel}
$$

87. Wellencharakter von Teilchen:
$$
\begin{array}{|c|c|}
\hline \lambda  &  = & \frac{h}{p}  \\
\hline E_{\text{kin}} &  = & hf  \\
\hline 
\end{array}
$$
88. Wellenlänge der Elektronen:
$$
\lambda  =  \frac{h}{\sqrt{ 2mE_{\text{kin}} }}  =  \frac{h}{\sqrt{ 2meU }}
$$
89. Wellenfunktion:
$$
\boxed{ E  =  \hbar \omega}
$$
$$
\boxed{\vec{p}  =  m\vec{v}  =  \hbar \vec{k}}
$$
$$
\boxed{ \psi(x,t)  =  \mathcal{C} \cdot \exp\left( \frac{i}{\hbar}(Et+px) \right)}
$$

90. Phasen geschwindigkeit in mat. Wellen:
$$
\begin{array}{|c|c|}
 \hline \text{Photon} & v_{\text{ph}}  =  \frac{E}{p}  =  c \\
\hline \text{Materie} & v_{\text{ph}}  =  \frac{\hbar}{2m}k \\
\hline
\end{array}
$$
91. Wahrscheinlichkeit interpretation:
$$
\boxed{W(\vec{r},t)  =  | \psi(\vec{r},t) |^{2} d(x,y,z)}
$$


92. Unschärfe relationen:
$$
\boxed{\Delta x \cdot \Delta p \geq \frac{\hbar}{2}}
$$
$$
\boxed{ \Delta E \cdot \Delta t \geq \frac{\hbar}{2}}
$$
93. Schrödingergleichung:
$$
-\frac{\hbar^{2}}{2m} \frac{ \partial^{2} \psi }{ \partial x^{2}}+V\psi(x)=  E\psi(x)
$$
