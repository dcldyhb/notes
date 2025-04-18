# Schrodinger Equation Application

## 1-D finite

- potential well

$$
\begin{aligned}
    V(x)=
    \begin{cases}
        0, & |x|<\frac{d}{2} \\
        V_0, & |x|>\frac{d}{2}
    \end{cases}
\end{aligned}
$$

- outside well

$$
\begin{gathered}
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+V_0\psi(x)=E\psi(x)\\
\Rightarrow \frac{d^2\psi(x)}{dx^2}=\frac{2m}{\hbar^2}(V_0-E)\psi(x)\\
\end{gathered}
$$

The solution should be exponential equation:

$$
\Psi (x) = 
\left\{
\begin{array}{ll}
    A_{+}e^{k' x}, & x\leq-\frac{d}{2} \\
    A_{-}e^{k' x}, & x\geq\frac{d}{2}
\end{array}
\right.
$$

## Tunel effect

![Tunel effect](https://raw.githubusercontent.com/dcldyhb/Freshman-Notes-Image-Host/main/202504181642705.png)

$$
V(x)=
\left\{
\begin{array}{ll}
    0, & x < x_1 \quad \text{or} \quad x > x_2 \\
    V_0, & x_1 < x < x_2
\end{array}
\right.
$$

Classically , if $E<V_0$, the partide will be totally reflected back.
However , **quantum mechanics** will give a different result.


$$
\frac{d^2\psi(x)}{dx^2}=\frac{2m}{\hbar^2}(V_0-E)\psi(x)
$$

general solution is:

$$
\Psi (x) = Ae^{-k x} + Be^{k x}
$$

For region Ⅰand Ⅲ, $V_0 - E < 0$, $k$ is imaginary, so $\Psi(x)$ is a prapagatory wave.
For region Ⅱ, $V_0 - E > 0$, $k$ is real, so $\Psi(x)$ is a exponential decay ray.

### probability of tunnel effect

$$
P = \left\vert \frac{\Psi(x_2)}{\Psi(x_1)} \right\vert^2 = e^{-2kD} = e^{-\frac{2}{\hbar}\sqrt{2m(V_0-E)}D}
$$

P deacays exponentially with the width of the barrier $D$. **Very sensitive**.

With this effect, we developped STM.

## 1-D harmornic oscillator

$$
\begin{gathered}
    F(x) = -kx \\
    V(x) = \frac{1}{2}kx^2 = \frac{1}{2}m\omega^2x^2 \quad (\omega = \sqrt{\frac{k}{m}}) 
\end{gathered}
$$

Schrödinger equation:

$$
\begin{gathered}
    &-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} \psi(x)+ \frac{1}{2}m\omega^2x^2\psi(x) = E\psi(x) \\
    &\Rightarrow  \left\{
\begin{array}{ll}
   E_n= (n+\frac{1}{2})\hbar\omega\\
   \Psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^\frac{1}{4}(2^n\cdot n!)e^{-\frac{m\omega}{2\hbar}x^2}H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right) \\
\end{array}
\right.
\end{gathered}
$$

> **Notes**
> Scanning tunnenling microscopy invented by Binnig and Rohrer in 1981.
