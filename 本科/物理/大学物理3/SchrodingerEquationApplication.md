---
title: Schrodinger Equation Application
category:
  - 专业课程
  - 物理
tags:
  - 物理
  - 量子力学
  - 课程笔记补充
math: true
hide: true
date: 2025-4-18 16:24:28
---

# Schrodinger Equation Application

## 1-D finite square well

$$
V(x) =
\begin{cases}
    0 , & |x|<\frac{d}{2} \\
    V_0 , & |x|>\frac{d}{2}
\end{cases}
$$

- inside the well

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x)
$$

set $k^2 = \frac{2mE}{\hbar^2}$

$$
\begin{cases}
\frac{\mathrm{d}^2\Psi}{\mathrm{d}x^2} = -k^2\Psi\\
\Psi  = A\sin(kx) + B\cos(kx)\\
\end{cases}
$$

- potential well

$$
V(x)=
\begin{cases}
    0, & |x|<d \\
    V_0, & |x|>d
\end{cases}
$$

$$
\Psi = A \sin(kx+\delta)
$$

from the boundary condition, we have:

$$
\begin{cases}
    \Psi(0) = 0 \\
    \Psi(d) = 0
\end{cases}
$$

$$
\begin{cases}
    \delta = 0\\
    k = \frac{n\pi}{d}
\end{cases}
\Rightarrow
\begin{cases}
    \Psi_n(x) = A\sin(\frac{n\pi}{d}x)\\
    E_n = \frac{n^2h^2}{8m^2d^2}
\end{cases}
$$

$\Psi$ should be normalized, so

$$
\int_{-\infty}^{+\infty}\vert \Psi_n(x)\vert^2 \mathrm{d}x = A^2 \frac{d}{2} = 1 \Rightarrow A = \sqrt{\frac{2}{d}}
$$

$$
\Psi_n(x) = \sqrt{\frac{2}{d}}\sin(\frac{n\pi}{d}x)
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
\begin{cases}
    A_{+}e^{k' x}, & x\leq-\frac{d}{2} \\
    A_{-}e^{k' x}, & x\geq\frac{d}{2}
\end{cases}
$$

## Tunel effect

![Tunel effect](https://raw.githubusercontent.com/dcldyhb/Freshman-Notes-Image-Host/main/202504181642705.png)

$$
V(x)=
\begin{cases}
    0, & x < x_1 \quad \text{or} \quad x > x_2 \\
    V_0, & x_1 < x < x_2
\end{cases}
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

in which $k = \sqrt{\frac{2m(V_0-E)}{\hbar^2}}$.

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
    &\Rightarrow
\begin{cases}
   E_n= (n+\frac{1}{2})\hbar\omega\\
   \Psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^\frac{1}{4}(2^n\cdot n!)e^{-\frac{m\omega}{2\hbar}x^2}H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right) \\
\end{cases}
\end{gathered}
$$

> **Notes**
>
> 1. $E_0 = \frac{1}{2}\hbar\omega > 0$ . There is no absolute rest.
> 2. $\Delta E = \hbar\omega$. Similar to photons. There is the basisi for Plank's hypothesis on energy quanta.

## Schrodinger equation for hydrogen atom

central force field:

$$
V(r) = -\frac{Ze^2}{4\pi\epsilon_0r} = -\frac{e^2}{4\pi\epsilon_0r}
$$

$$
\frac{\mathrm{d}\vec{L}}{\mathrm{d}t} = \vec{r} \times \vec{F} = \vec{0}
$$

$\vec{L}$ is a constant vector.

Schrödinger equation:

$$
\left[-\frac{\hbar^2}{2m}\nabla^2+U(\vec{r})\right]\Psi(\vec{r})=E\Psi(\vec{r})
$$

The Coulamb potential has spherical symmetry, so we can use spherical coordinates $(r , \theta , \phi)$.

set

$$
\begin{cases}
    x = r\sin{\theta}\cos{\phi} \\
    y = r\sin{\theta}\sin{\phi} \\
    z = r\cos{\theta}
\end{cases}
$$

$$
\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin{\theta}}\frac{\partial}{\partial \theta}\left(\sin{\theta}\frac{\partial}{\partial \theta}\right) + \frac{1}{r^2\sin^2{\theta}}\frac{\partial^2}{\partial \phi^2} \equiv \hat{L}^2
$$

$$
-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) \Psi(\vec{r})+ \frac{1}{r^2\sin{\theta}}\frac{\partial}{\partial \theta}\left(\sin{\theta}\frac{\partial}{\partial \theta}\right) \Psi(\vec{r})+ \frac{1}{r^2\sin^2{\theta}}\frac{\partial^2}{\partial \phi^2}\Psi(\vec{r})\right] - \frac{Ze^2}{4\pi\epsilon_0r}\Psi(\vec{r}) = E\Psi(\vec{r})
$$

set $\Psi(\vec{r}) = R(r)Y(\theta , \phi)$

$$
\frac{1}{\hbar^2}\hat{L}^2Y = \frac{1}{R}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}}{\mathrm{d}r}R\right)+\frac{2mr^2}{\hbar^2}(E-V(r)) = const.
$$

The solution $\displaystyle \Psi_{n,m,l}(r , \theta , \phi) = R_n(r)Y_{l,m}(\theta , \phi)$ is function of $\hat{H},\hat{L^2},\hat{L_z}$.

$$
\begin{cases}
    \hat{H}\Psi_{n,m,l} = \frac{E}{n^2}\Psi_{n,m,l} \\
    \hat{L^2}\Psi_{n,m,l} = l(l+1)\hbar^2\Psi_{n,m,l} \\
    \hat{L_z}\Psi_{n,m,l} = m\hbar\Psi_{n,m,l}
\end{cases}
$$

- **n**
  - The peinciple quantum number describing the size of the orbit as well as the energy of the orbit.
  - $\Psi_{n,0}$ has $(n-1)$ nodes
  - $n = 1,2,3,\cdots$

![pic](https://raw.githubusercontent.com/dcldyhb/Freshman-Notes-Image-Host/main/202504251621261.png)

- **l**
  - The angular momentum quantum number describing the shape of the orbit.
  - $l = 0,1,2,\cdots,n-1$
- **m**
  - The magnetic quantum number describing the orientation of the orbit.
  - $m = 0 ,\pm 1 , \pm 2 , \cdots , \pm l$

[goback](/README.md)
