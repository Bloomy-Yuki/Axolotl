## Misc
1. open interval:
$$
(a,b) :  =  \{ x \in \mathbb{R}: a < x <b \}
$$
2. closed interval:
$$
[a,b] := \{ x \in \mathbb{R} : a \leq x \leq b \}
$$

3. Bernoulli inequality:
$$
\boxed{ \forall n \in \mathbb{N}_{0}, \forall a\geq-1 \in \mathbb{R}:}\, \, 
$$
$$
\boxed{ (1+a)^{n} \geq 1+na}
$$
4. Geometric summation formula:
$$
\begin{array}{|c|c|}
\hline \sum_{k=1}^{n} q^{k} & 1+q+q^{2}+\dots+q^{n} & \frac{1-q^{n+1}}{1-q} \\
\hline \sum_{k=1}^{n} a^{k}b^{n-k} & b^{n}+ab^{n-1} +a^{2}b^{n-2}+\dots+a^{n} & \frac{a^{n+1} -b^{n+1}}{a-b} \\
\hline
\end{array}
$$
5. Binomial coefficient rules:
$$
\begin{array}{}
\begin{pmatrix}
n \\
k 
\end{pmatrix}  =  \begin{pmatrix}
n \\
n-k
\end{pmatrix} \\
 \\
\begin{pmatrix}
n \\
k -1
\end{pmatrix} + \begin{pmatrix}
n \\
k
\end{pmatrix}  =  \begin{pmatrix}
n+1 \\
k
\end{pmatrix}, k>0 \\
 \\
\end{array}
$$
6. Binomial formula:
$$
\boxed{\forall n \in \mathbb{N}_{0}, \forall a,b \in \mathbb{C}:} \, \, 
$$
$$
\boxed{\boxed{(a+b)^{n}  =  \sum_{k=0}^{n} \begin{pmatrix}
n \\
k
\end{pmatrix} a^{k} b^{n-k}   =  \sum_{k=0}^{n} \begin{pmatrix}
n \\
k
\end{pmatrix} b^{k} a^{n-k} }}  
$$
7. inequality between geometric and arithmetic average:
$$
\boxed{ \forall n \in \mathbb{N}, a_{1},a_{2},\dots a_{n} \in \mathbb{R}_{+}}
$$
$$
\sqrt[n]{ a_{1} \cdot a_{2} \cdot \dots \,  \cdot a_{n}}\leq \frac{1}{n}(a_{1}+a_{2}+\dots +a_{n})
$$
8. inequality properties:
$$
\begin{array}{|c|c|}
\hline a+c <b+c  &  \iff & a<b \\
\hline (a<b )\land ( \Theta\leq \Pi)  & \iff & a+ \Theta <b+\Pi \\
\hline (a<b )\land ( 0 <\Theta\leq \Pi)  & \iff & a\cdot \Theta <b\cdot\Pi \\
\hline a<b & \iff & -b <-a \\
\hline 0<a<b  & \iff  & 0<\frac{1}{b}  <\frac{1}{a}\\ 
\hline
\end{array}
$$
9. Clopen sets:
$$
\begin{array}{|c|c|}
\hline \forall A \ne \emptyset \subset \mathbb{R}:  & A \text{ (not closed)} \centernot \implies A \text{ (open)}  \\
\hline    
\end{array}
$$
$$
\mathbb{R}, \emptyset \text{ are both closed and open (clopen)!}
$$

## Completeness

10. Triangle inequality:
$$
\boxed{\begin{gather}
\forall a,b \in \mathbb{C}\\
| a | -| b | \leq | | a | -| b | | \leq| a + b | \leq | a | + | b |
\\ \\ \forall x,y,z ,\dots \,  \in \mathbb{C} : \,  \, \\ 
| x + y +z + \dots | \leq | x | + | y | +| z |+\dots
\end{gather} }
$$
11. Equality definition:
$$
\begin{gather}
\forall a, b  \in \mathbb{C}\\
a = b \iff \forall \epsilon >0 \in \mathbb{R}, | a-b | <\epsilon
\end{gather}
$$
12. Axiom of completeness:
$$
\boxed{\boxed{\begin{gather}
\forall A \neq \emptyset \subseteq \mathbb{R},\\
(\exists s \in \mathbb{R},\forall x \in A,  \space \space  s \geq x) \implies (\exists! X \in \mathbb{R}, X = \sup A )
\end{gather}}}
$$ ^72b4d8
13. Nested interval property:
$$
\begin{gather}
\forall n \in \mathbb{N},
\\
I_{n}  = [a_{n},b_{n}] = \{ x \in \mathbb{R} : a_{n }\leq x \leq b_{n}\},\\
I_{n+1} \subseteq I_{n}\\
\\
\bigcap_{n = 1}^{\infty}I_{n} \neq \emptyset
\end{gather}
$$
14. Archimedean property:
$$
\begin{gather}
\text{1) }\forall x \in \mathbb{R}, \exists n \in \mathbb{N}: n >x
\\
\text{2) } \forall x \in \mathbb{R}, \exists n \in \mathbb{N}, \frac{1}{n}<x
\end{gather}
$$
15. Density of $\mathbb{Q}$ in $\mathbb{R}$:
$$
\begin{gather}
\forall a,b \in \mathbb{R}:\\ (a<b) \implies (\exists x \in \mathbb{Q},a < x <b)
\end{gather}
$$
16. Schröder-Bernstein Theorem:
$$
\boxed{\begin{gather}
\exists  f : X \to Y \text{ Injektiv}\\
\exists  g : Y \to X \text{ Injektiv}\\ 
\end{gather}} \implies \exists  \phi : X \to Y \text{ Bijektiv}
$$
17. Cantor theorem:

$$
\begin{array}{|c|c|}
\hline \forall X,\forall \Psi \in \mathcal{P}(X) ^{X},\exists \Upsilon \in \mathcal{P}(X): \,  \\
\hline \forall x \in X, \Psi(x) \ne \Upsilon \\
\hline
\end{array}
$$

## Sequences

18. Sequence definition:
$$
\begin{gather}
\text{ Sequence / Folge $(a)_{n}$ in } S: \ \,  \, \\
 a : \mathbb{N} \to S, \space n \mapsto a_{n}
\end{gather}
$$
19. Convergence of a Sequence:
$$
\begin{gather}
\text{sequence $(a)_{n}$ converges to  }x\\
 \lim_{ n \to \infty } a_{n }= x
\\
\iff \\ \forall \epsilon >0 \in \mathbb{R}, \exists L \in \mathbb{N}:\\ \forall n \geq L \in \mathbb{N}.| a_{n} -x| <\epsilon
\end{gather}
$$
20. Supremum analytically:
$$
\begin{gather}
\forall A \subseteq \mathbb{R}, \sup A = X\\
\iff (\forall a \in A,  X \geq a )\land(\forall\epsilon >0 \in \mathbb{R}, \exists a \in A,  \space \space X-a   < \epsilon)
\end{gather}
$$
21. Neighborhood in $\mathbb{R} / \mathbb{C}$ :
$$
\begin{gather}
 V_{\epsilon}(x)  = \{ z \in (\mathbb{R} / \mathbb{C}) : | z-x | < \epsilon\}
\\\\
\boxed{\epsilon >0 \in \mathbb{R}}
\end{gather}
$$
22. Bounded Sequence def. : 
$$
\begin{gather}
\text{ Bounded sequence $(a)_{n}$:}\\
\iff \exists M \in \mathbb{R}, \forall n \in \mathbb{N}, | a_{n} | \leq M
\end{gather}
$$
23. Algebraic limit theorem:
$$
\begin{gather}
\boxed{\lim a_{n} = A, \lim b_{n} = B}\\
\\
1 .  \space \space  \forall c \in \mathbb{R}, \lim(c a_{n}) = c A\\
2 .  \space \space \lim(a_{n}+b_{n}) = A+B\\
3 .  \space \space \lim(a_{n} b_{n} ) =  AB\\
4 .  \space \space  \lim\left( \frac{a_{n}}{b_{n}} \right) = \frac{A}{B}, B \neq 0
\end{gather}
$$
24. Order limit theorem:
$$
\begin{gather}
\boxed{\lim a_{n} = A, \lim b_{n} = B}\\
1 .  \space \space \forall n \in \mathbb{N}, (a_{n} \geq0) \implies A\geq0\\
2 .  \space \space  \forall n \in \mathbb{N}, (a_{n }\leq b_{n}) \implies A \leq B\\
3 .  \space \space  \forall c \in \mathbb{R}, \forall n \in \mathbb{N}, (a_{n} \geq c) \implies A\geq c\\
\end{gather}
$$
25. squeeze theorem:
$$
\boxed{\begin{gather}
 \forall n \in \mathbb{N}, a_{n}\leq b_{n} \leq c_{n}\\
\land \\
 \lim a_{n } = \lim c_{n} = X
\end{gather}} \implies \lim b_{n}  = X
$$
26. Monotone def. :
$$
\begin{gather}
\boxed{ \text{ Monotone increasing:}}\\
\forall n \in \mathbb{N}, a_{n+1} \geq a_{n}\\
\\
\boxed{ \text{ Monotone decreasing:}}\\
\forall n \in \mathbb{N}, a_{n+1} \leq a_{n}
\end{gather}
$$
27. Monotone convergence theorem:
$$
\boxed{\begin{gather}
(a)_{n} \text{ is bounded}\\
\land \\
(a)_{n} \text{ is monotone}
\end{gather}} \implies (a)_{n} \text{converges}
$$

28. Subsequence def. :
$$
\begin{gather}
(a)_{n} \text{ is a sequence}\\
(n)_{k}: \mathbb{N} \to \mathbb{N} \text{ is a sequence with }  \forall k \in \mathbb{N}:n_{k+1} >n_{k}\\
\\
(a)_{n_{k}} \text{ is subsequence of $(a)_{n}$}\\
\end{gather}
$$

29. Convergence through subsequences:
$$
(a)_{n}  \,  \text{conv.} \iff \text{ all subseq. conv.}
$$

30. Existence of monotone subsequences:
$$
\boxed{\text{ every real sequence has a monotone subseq.}}
$$

31. Bolanzo-Weierstraß theorem ($\mathbb{R} / \mathbb{C}$):
$$
\boxed{\begin{gather}
\boxed{\begin{gather}
\text{ Bounded sequence $(a)_{n}$:}\\
\iff \exists M \in \mathbb{R}, \forall n \in \mathbb{N}, | a_{n} | \leq M
\end{gather}} \\ 
\implies 
\\ 
\boxed{
\begin{gather}
\exists(a)_{n_{k}}
\end{gather} \text{ conv. subseq. }}
\end{gather}}_{\mathbb{ (R /C)}}
$$
32. Cauchy sequence:
$$
\begin{gather}
\text{ Cauchy sequence :}\\
\\
\forall \epsilon >0 \in \mathbb{R}, \exists L \in \mathbb{N}:\\
\forall m,n \geq L \implies | a_{n} -a_{m} | < \epsilon
\end{gather}
$$
33. Cauchy criterion:
$$
\boxed{\begin{gather}
(a)_{n} \text{ conv.} \iff (a)_{n} \text{ is Cauchy seq.} 
\end{gather}}
$$
34. Completeness implications:
$$\begin{gather}\boxed{\text{AoC} \implies \begin{cases}\text{NIP} \implies\text{BW} \implies \text{CC} \\\space \space  \\\text{MCT} \end{cases}} \\ \\ \begin{array}{|c|c|}\hline\text{AoC:} &  \text{Axiom of Completeness}\\
\hline\text{NIP:} &  \text{Nested Interval Property}\\\hline\text{MCT:} & \text{Monotone Convergence Theorem}\\
\hline\text{BW:}  & \text{Bolanzo-Weierstraß Theorem}\\
\hline\text{CC:}  & \text{Cauchy Convergence Criterion} \\\hline \end{array}\end{gather}$$

## Complex numbers

35. Set of complex numbers:
$$
\begin{gather}
\mathbb{C} := \{ z  = x + iy : \forall x,y \in \mathbb{R} \}\\
i:= + \sqrt{ -1 }
\\
\\
\mathrm{Re } (z) = x\\
\mathrm{Im} (z)  = y\\
\bar{z} := x - iy \text{ complex conjugate}
\end{gather}
$$

36. Properties of complex conj. and abs. value:
$$
\begin{gather}
\forall z,w \in \mathbb{C}:\\
\boxed{\mathrm{Re}(z) = \frac{1}{2}(z +\bar{z}), \mathrm{Im}(z) = \frac{1}{2i}(z-\bar{z})}\\
\boxed{\overline{z+w}  = \overline{z} + \overline{w}}\\
\boxed{\overline{z \cdot w}  =  \overline{z} \cdot \overline{w}}\\
\boxed{\overline{\left( \frac{z}{w} \right)}  =  \frac {\overline{z}} {\overline{w}}, w \neq 0}\\
\boxed{ \overline{\overline{z}}  = z}\\
\boxed{ z \cdot \overline{z}  = | z |^{2}  = \mathrm{Re}(z)^{2} + \mathrm{Im}(z)^{2} \geq0}
\\
z  =  \overline{ z} \iff z \in \mathbb{R}
\end{gather}
$$
37. absolute complex properties:
$$
\begin{gather}
\forall z , w \in \mathbb{C}:\\
|  \mathrm{Re}(z)|\leq | z |, |\mathrm{Im}(z)| \leq | z |,\\
|\mathrm{Re}(z)| + |\mathrm{Im}(z)| \geq | z |
\\
\\
| z |  =  0 \iff z  = 0\\
| z \cdot w |  =  | z | \cdot | w |, | \frac{z}{w} |  =  \frac{|  z|}{| w |}\\
\frac{1}{z}  = \frac{\overline{z}}{| z |^{2}}
\\\\
\text{triangle inequality:}\\
\\
| z +w | \leq | z | + | w |\\
| | z |-| w | | \leq | z-w |
\end{gather}
$$
## Series
38. Series definition:
$$
\begin{gather}
\text{ series is a sequence: }:\\
\\
s_{n}: n \mapsto \sum_{i=1}^{n} a_{i}\\
(a)_{i} \text{ is a sequence of $\mathbb{R} / \mathbb{Q}$}\\
\boxed{\sum_{i=1}^{\infty} a_{i }  =  A \iff \lim s_{n}  = A}\\
\end{gather}
$$
39. Algebraic limit theorem for series:
$$
\begin{gather}
\boxed{\sum_{i=1}^{\infty} a_{i}  =  A, \sum_{i=1}^{\infty}b_{i}  = B }\\
\\
\text{1) }\sum_{i=1}^{\infty} c \cdot a_{i}  =  c \cdot A\\
\text{2) } \sum_{i=1}^{\infty} (a_{i}+ b_{i})  =  A + B
\end{gather}
$$
40. Cauchy criterion for series:
$$
\begin{gather}
\sum_{i=1}^{\infty} a_{i}  \text{ conv.}\\
\iff \forall\epsilon >0 \in \mathbb{R}, \exists L \in \mathbb{N}:\\
\forall n >m\geq L\in \mathbb{N}:\\
| s_{n} - s_{m} | < \epsilon
\end{gather}
$$
41. Convergence and zero asymptote:
$$
\sum_{i=1}^{\infty} a_{i } \text{ conv. } \implies \lim a_{i}  = 0
$$
42. Series comparison test:
$$
\boxed{
\begin{gather}
(a)_{n}, (b)_{n} \text{ are seq. with}\\
\forall n \in \mathbb{N}: 0 \leq a_{n} \leq b_{n}
\end{gather}
}
$$
$$
\begin{gather}
 \implies \begin{cases}
\sum_{n=1}^{\infty} b_{n} \text{ conv.} \implies \sum_{n=1}^{\infty} a_{n} \text{ conv.} \\
\\
\sum_{n=1}^{\infty} a_{n} \text{ diver.} \implies \sum_{n=1}^{\infty} b_{n} \text{ diver.}
\end{cases}
\end{gather}
$$

43. Absolute convergence test:
$$
\begin{gather}
\sum_{i=1}^{\infty} |a_{i}| \text{ conv.} \implies \sum_{i=1}^{\infty} a_{i} \text{ conv.}
\end{gather}
$$
44. Alternating series test:
$$
\begin{gather}
(a)_{n} \text{ seq. with:}\\
\bullet  \space \space a_{n+1} \leq a_{n} \\
\bullet  \space \space \lim (a)_{n}  =  0\\
\\
\implies \sum_{n=1}^{\infty} (-1)^{n+1}a_{n} \text{ conv.}
\end{gather}
$$
45. Absolute vs. conditional convergence:
$$
\begin{gather}
\boxed{ \text{Absolute Convergence:}}\\
\sum_{i=1}^{\infty} |a_{i}| \text{ conv.}\\
\\ \boxed{\text{Conditional Convergance:}}\\
\sum_{i=1}^{\infty}a_{i} \text{ conv.} \land \sum_{i=1}^{\infty} |a_{i}| \text{ diver.}\\ 
\end{gather}
$$
46. Rearrangements definition:
$$
\begin{gather}
\text{ rearrangement of } \sum_{i=1}^{\infty} a_{i}:\\
f \in \mathbb{N}^{\mathbb{N}} \text{ (bijektiv)}\\
\\
\\
\sum_{i=1}^{\infty} a_{f(i)}  =  \sum_{i=1}^{\infty} b_{i}\\
\boxed{ \text{ called a rearrangement of sum}}
\end{gather}
$$

47. absolute convergence implies rearrangement convergence:
$$
\begin{gather}
\sum_{i=1}^{\infty} |a_{i}| =  A \\
\implies \forall f(\text{ bijektiv}) \in \mathbb{N}^{\mathbb{N}} : \sum_{i=1}^{\infty} a_{f(i)}  = A
\end{gather}
$$
48. Summation by parts:
$$
\begin{gather}
(a)_{i}, (b)_{i} \text{ seq. with:}\\
a_{0} = b_{0} = 0\\
\Delta a_{i}  =  a_{i+1} - a_{i} \\
\Delta b_{i}  =  b_{i+1} - b_{i} \\
\\
\sum_{i=m}^{n} b_{i} \cdot \Delta a_{i}  =  (a_{n+1}b_{n+1} -a_{m}b_{m}) - \sum_{i=m}^{n} \Delta b_{i} \cdot a_{i+1}
\end{gather}
$$
49. Root test for series:
$$
\boxed{\begin{gather}
\sum_{i=1}^{\infty} a_{k}  \text{ conv.} \iff \lim_{ n \to \infty } \sqrt[n]{  |a_{n}|}  \,  <1
\end{gather}}
$$
50. Abel test :
$$
\boxed{\begin{gather}
\sum_{i=1}^{\infty} a_{i} \text{ conv.}\\
\land \\
(b)_{i}: \forall i \in \mathbb{N}, b_{i+1} \leq b_{i}
\end{gather}}\implies \boxed{
\begin{gather}
\sum_{i=1}^{\infty} a_{i} \cdot b_{i } \\
\text{ is conv.}
\\
\end{gather}
}
$$
51. Harmonic series:
$$
\begin{gather}
S  =  \sum_{x = 1}^{\infty} \frac{1}{x} = \infty \\
S_{n} \approx \ln(n) + \gamma \\
\\
\gamma  = 0.57…
\end{gather}
$$
52. Cauchy condensation test:
$$
\begin{gather}
\forall n \in \mathbb{N},(a_{n} \geq 0 ) \land ( a_{n+1} \leq a_{n}): \ \,\\
\\a_{n} \text{ conv.} \iff \sum_{n = 0}^{\infty}2^{n}a_{2^{n}} \text{ conv.}
\end{gather}
$$

53. Dirichlet test:
$$
\boxed{\begin{gather}
\exists L \in \mathbb{R}, \forall n \in \mathbb{N},\sum_{i=1}^{n} a_{i}  = s_{n} \leq L \\
 \text{(bounded)}\\
 \land \\
(b)_{i}: \forall i \in \mathbb{N}, b_{i+1} \leq b_{i} \land \lim(b)_{i}  = 0
\end{gather}} \implies \boxed{
\begin{gather}
\sum_{i=1}^{\infty} a_{i} \cdot b_{i} \\
\text{ is convergent}
\end{gather}
}
$$

## Topology


54. Open set def. :
$$
\begin{gather}
O \subseteq \mathbb{R} \text{ is Open:}\\
\forall x \in O,\exists\epsilon > 0 \in \mathbb{R}:\\
V_{\epsilon} := (x-\epsilon, x+ \epsilon) \subseteq O
\end{gather}
$$
55. accumulation / limiting points:
$$
\begin{gather}
A \subseteq \mathbb{R} \text{ has limiting point $x$ if:}\\
\exists(a)_{i} : \mathbb{N} \to A \setminus \{ x \}:\\ \lim (a)_{i} = x
\\
\text{ otherwise $x \in A$  is called isolated point}
\end{gather}
$$

56. closed set def. :
$$
\begin{gather}
\\
\boxed{A \subseteq \mathbb{R}  \text{ is closed}}\\
\iff \\
\mathcal{H}_{a} \subseteq A\\
\mathcal{H}_{A}  =  \{ a : a \text{ is limiting point of A} \}
\end{gather}
$$
57. Cauchy condition for closed sets:
$$
\begin{gather}
A \subseteq \mathbb{R}\\
A \text{ is closed }\\
\iff \\
\text{ every Cauchy seq. on $A$ converges}
\end{gather}
$$
58. Closure def. and properties:
$$
\begin{gather}
\text{ Closure of } A \subseteq \mathbb{R}:\\
A \cup \mathcal{H}_{A}  =  \overline{A}\\
\overline{A}  = \overline{\overline{A}}\\
\\
\text{Closure is closed}
\end{gather}
$$
59. complement of sets:
$$
\begin{gather}
\forall A \subseteq \mathbb{R}:\\
A \text{ closed} \iff A^{C} \text{ open}\\
A \text{ open} \iff A^{C} \text{ closed}\\
\\
\emptyset, \mathbb{R} \text{ are both open and closed}
\end{gather}
$$
60. union and intersection of open / closed sets:
$$
\begin{gather}
\forall i \in \mathbb{N}\\\\
\boxed{\text{ $A_{i}$ Open:}}\\
\bigcap^{n} A_{i}  \text{ open}\\
\bigcup A_{i} \text{ open}\\
\\
\boxed{ A_{i}  \text{ Closed:}}\\
\bigcap A_{i} \text{ closed}\\
\bigcup^{n} A_{i} \text{ closed}
\end{gather}
$$
61. Open cover definition:
$$
\boxed{A \text{ is a Set}}
$$
$$
\begin{array}{|c|c|}
\hline \text{Cover:}  & \{ U_{\alpha} \}_{\alpha \in I}  & A \subseteq \bigcup_{\alpha \in I} U_{\alpha}\\ 
\hline \text{Open Cover:} & \forall U_{\alpha} \in \{ U_{\alpha} \}_{\alpha \in I}, U_{\alpha} \text{ is Open} &  \\ 
\hline \text{finite Subcover:}  & \exists \mathcal{F } \subseteq I, | \mathcal{F}  |< \aleph_{0}:  & A \subseteq \bigcup_{\alpha \in \mathcal{F}} U_{\alpha} \\
\hline
\end{array}
$$
62. Compact definitions and Heine-Borel:
$$
\boxed{ A \text{ Compact}: \text{Every Open cover has finite subcover for } A}
$$
$$
\begin{array}{|c|c|}
\hline \text{ Heine-Borel Theorem:} &  \text{ Compact} \\
\hline  A \text{ is Compact} & \iff \\
\hline A \text{ Closed and bounded} & \iff \\
\hline \text{ All sequences in A have conv. subseq.} &  \iff \\
\hline \text{ Every open cover of } A \text{ hasa finite subcover} &  \iff \\
\hline
\end{array}
$$
63. Perfect Set definition:
$$
\begin{gather}
\boxed{ A \subseteq \mathbb{R} \text{ is perfect} \iff A \text{ is closed with no islolate points}}\\
\boxed{\forall A \subseteq \mathbb{R}, A \text{ is perfect}, | A |  =  \aleph_{1}}
\end{gather}
$$
64. Separated, disconnected, and connected Set definitions :
$$
\begin{array}{|c|c|}
\hline A,B\text{ are separated} \iff &  A,B \ne \emptyset\subset \mathbb{R}    :& (A \cap \overline{B}  = \emptyset) \land(\overline{A}\cap B  = \emptyset) \\
\hline  E \text{ is disconnected}  \iff& E\subset \mathbb{R}, \exists A,B \ne \emptyset \subset E, \, E  = A \cup B  :&  (A \cap \overline{B}  = \emptyset) \land(\overline{A}\cap B  = \emptyset) \\ 
\hline E \text{ is connecteed} \iff  & E \subset \mathbb{R}, \forall A,B \ne \emptyset \subset E , \,  E  =  A \cup B:  & (A \cap \overline{B} \ne \emptyset) \lor(\overline{A} \cap B \ne \emptyset)\\ 
\hline E \text{ is connected } \iff  & E \subset \mathbb{R}, \forall A,B \ne \emptyset \subset E , \,  E  =  A \cup B: & (\exists (a)_{n} \in A^{\mathbb{N}} \lor \exists(a)_{n} \in B^{\mathbb{N}}) \land ((\lim (a)_{n} \in B) \lor (\lim (a)_{n} \in A)) \\
\hline E \text{ is connected} \iff & \forall a,b \in E:  &  (a<c<b) \implies (c \in E) \\
\hline
\end{array}
$$

## Continuity

65. Definition of functional limit at $x_{0}$ :
$$
\boxed{  f : A \to \mathbb{R}, x_{0} \text{ is limiting point of } A}
$$
$$
\boxed{ \lim_{ x \to x_{0} } f(x)  =  L}
$$
$$
\boxed{\boxed{\forall\epsilon >0, \exists \delta >0, \forall x \in A:| x -x_{0} |< \delta \implies | f(x) - L | < \epsilon}}
$$
66. Limits mean convergence of every sequence in $A$ : 

$$
\boxed{  f : A \to \mathbb{R}, x_{0} \text{ is limiting point of } A}
$$
$$
\boxed{\begin{gather}
\lim_{ x \to x_{0} } f(x)  = L \\
\iff \\
\text{ Every seq.} (a)_{n}, a_{n} \neq x_{0} \text{ in } A\\
\text{and } \lim (a)_{n}  = x_{0}: \lim f(a_{n})  =  L  
\end{gather}}
$$
67. Functional limits laws:
$$
\boxed{ f,g: A \to \mathbb{R}, A \subseteq \mathbb{R}}
$$
$$
\begin{array}{|c|c|}
\hline \lim_{ x \to x_{0}} f(x)  =  L & \lim_{ x \to x_{0} } g(x)  =  M \\
\hline
\end{array}
$$
$$
\begin{array}{|c|c|}
\hline \lim_{ x \to x_{0} } k \cdot f(x) &  =   & k \cdot L \\ 
\hline \lim_{ x \to x_{0} } f(x) +g(x)  &   =  & L+M \\
\hline \lim_{ x \to x_{0} } f(x) \cdot g(x) &  =  & L \cdot M \\
\hline \lim_{ x \to x_{0} } \frac{f(x)}{g(x)}  &  =  & \frac{L}{M}, \forall x \in A, g(x) \neq 0 \\ 
\hline
\end{array}
$$
68. Functional Squeeze Theorem:
$$
\begin{array}{|c|c|}
\hline \forall x \in A \subseteq \mathbb{R}  \\
\hline f(x) <g(x) < h(x) \\
\hline
\end{array}
$$
$$
\begin{array}{|c|c|}
\hline \lim_{ x \to x_{0} } f(x)  =  L & \lim_{ x \to x_{0} } h(x)  =  L\\
\hline
\end{array}
$$
$$
\boxed{ \implies \lim_{ x \to x_{0} } g(x)  =  L}
$$
69. Continuous without Limit explicitly:
$$
\boxed{  f : A \to \mathbb{R}, x_{0} \text{ is limiting point of } A}
$$
$$
\boxed{ \forall\epsilon >0, \exists \delta >0, \forall x \in A: \, }
$$
$$
\boxed{| x-x_{0} |<\delta \implies | f(x) -f(x_{0}) |<\epsilon}
$$
70. Continuity Topologically, and sequentially:
$$
\boxed{\boxed{ \begin{gather}
f:A \to \mathbb{R}, x_{0} \text{ Limiting point of } A, \,  A \subseteq \mathbb{R} & \text{ Continuity:} \, \\
\hline f \text{ is Continuous at } x_{0} & \iff \\
\hline \forall\epsilon >0, \exists\delta >0, \forall x \in A: | x-x_{0} |  <\delta \implies | f(x) -f(x_{0}) | < \epsilon & \iff \\
\hline \forall \epsilon >0, \exists \delta >0, \forall x \in A: x \in V_{\delta}(x_{0}) \implies f(x) \in V_{\epsilon}(f(x_{0})) & \iff \\
\hline \forall (a)_{n}  \in A^{\mathbb{N}}, \,  \lim (a)_{n}  = x_{0} \implies \lim_{ } f((a)_{n})  =  f(x_{0}) & \iff \\
\hline x_{0} \text{ is Limit point of } A \implies \lim_{ x \to x_{0} } f(x)  =  f(x_{0}) & \iff
\end{gather}}}
$$
71. Continuity preserving Operations:
$$
\boxed{ f,g \text{ are Continuous}}
$$
$$
\implies
$$
$$
\begin{array}{|c|c|}
\hline k \cdot f(x)  \\
\hline f(x) + g(x) \\ 
\hline f(x) \cdot g(x)\\ 
\hline \frac{f(x)}{g(x)}, g(x) \ne 0 \\
\hline f \circ g \\
\hline \text{Conrinuous} \\
\hline
\end{array}
$$

72. Continuity and preimage condition:
$$
\boxed{f: A \to \mathbb{R}}
$$
$$
\begin{gather}
f \text{ is continuous} \\
\iff \forall B \text{ (Open)} \subseteq \mathbb{R}, f^{-1}(B)  = A \cap C \text{(Open)}
\end{gather}
$$
73. continuous compact image is continuous compact:
$$
\begin{gather}
\boxed{\boxed{ f: A \to \mathbb{R} \text{ is Continuous}}\\
\, \boxed{X \subseteq A \text{ is Compact}}}\\
\implies f(X) \text{ is Compact}
\end{gather}
$$
74. Extreme value theorem:
$$
\begin{array}{|c|c|}
\hline \forall f (\text{Contin.}):A \to \mathbb{R}, X \subseteq A ( \text{Compact})  & \implies & \exists a,b \in f(X) : \sup(f(X))  = a, \,  \inf(f(X))  = b \\
\hline
\end{array}
$$
75. Intermediate Value theorem:
$$
\begin{array}{|c|c|}
\hline\forall f(\text{Contin.}): [a,b] \to \mathbb{R}, f(a)<f(b):  & f(a)< L < f(b) \implies \exists x \in (a,b), f(x)  = L \\
\hline
\end{array}
$$
76. Preservation of Connected sets:
$$
\begin{array}{|c|c|}
\hline \forall f(Contin.): A\to \mathbb{R}, & \mathcal{C } \subseteq A \text{ is connected} \implies f(\mathcal{C}) \text{ is connecteed} \\
\hline
\end{array}
$$
77. Strictly monotone and surjective implies existence of inverse:
$$
\begin{array}{|c|c|}
\hline f(\text{Contin.}):A \to B, A,B \subseteq \mathbb{R} \\
\hline \forall x,y \in A, x<y \implies f(x)<f(y) \text{ (Mono.)}\\
\hline \forall z \in B, \exists w \in A: f(w)  = z \text{ (Surj. )} \\
\hline
\end{array} \implies \begin{array}{|c|c|}
\hline \exists f^{-1}(\text{Contin.}):B \to A \text{ (Bij.)}\\
\hline
\end{array}
$$
