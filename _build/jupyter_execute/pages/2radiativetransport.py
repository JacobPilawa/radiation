#!/usr/bin/env python
# coding: utf-8

# # Radiative Transport

# ## Radiative Transfer Equation

# ### Absorption

# Say some radiation $I_\nu$ passes through a region $ds$ of absorption/scattering on its way to us. Then:
# 
# $$
# dI_{\nu }=-\alpha _{\nu }I_{\nu }ds
# $$
# 
# where $\alpha_\nu$ is the extinction coefficient (units of $cm^{-1}$). We may compute $\alpha_nu$ a couple different ways:
# 
# $$
# \alpha_\nu = n \sigma_\nu = \rho \kappa_\nu
# $$
# 
# where:
# 
# * $n$ is the number density
# * $\sigma_\nu$ os the cross section
# * $\rho$ is the mass desnity
# * $\kappa_\nu$ is the opacity

# Solving for intensity, we find:
# 
# $$
# I_\nu(s) = e^{-n\sigma_\nu s} = e^{-\tau_\nu}
# $$
# 
# where $\tau_\nu$ is the optical depth at $\nu$. Optical depth is often computed as:
# 
# $$
# \tau_\nu = n \sigma_\nu s = N \sigma_\nu 
# $$
# 
# where $N$ is the column density of absorbers. Similarly, we have:
# 
# $$
# \tau_\nu = \rho \kappa_\nu s = \Sigma \kappa_\nu
# $$
# 
# where $\Sigma$ is the mass surface density and $\kappa_\nu$ is the density-weighted extinction coefficient. 
# 
# Note that when $\tau \gg 1$, we say it is **optically thick**, and when $\tau \ll 1$, we say we are **optically thin**. 
# 

# The **mean free path** is given by:
# 
# $$
# \lambda_\nu = \alpha_\nu^{-1} = \frac{1}{n\sigma_\nu} 
# $$
# 
# Thus, we have:
# 
# $$
# \tau_\nu = \frac{s}{\lambda_\nu}
# $$
# 
# That is, the optical depth is the number of mean-free-paths deep a medium is. For Poisson processes, the probability of absorption is given by:
# 
# $$
# P(n)={e^{-{s \over \lambda _{mfp,\nu }}}\left({s \over \lambda _{mfp,\nu }}\right)^{n} \over n!}
# $$
# 
# And therefore:
# 
# $$
# I_\nu(s) = I_\nu(0) e^{-\alpha_\nu s}
# $$

# ### Emission

# If $j_{\nu }$ is the emissivity, then the contribution of the emissivity of a medium to the flux is:
# 
# 
# $$
# {\displaystyle dI_{\nu }=j_{\nu }ds\,\!}{\displaystyle dI_{\nu }=j_{\nu }ds\,\!}
# $$

# ### Emission and Extinction Together

# $$
# {\displaystyle {{dI_{\nu } \over ds}=j_{\nu }-\alpha _{\nu }I_{\nu }}\,\!}
# $$
# 
# It is often convenient to express this in terms of optical depth. Dividing by $\alpha_\nu$ and recognizing $d\tau_\nu = \alpha_\nu \, ds$:
# 
# $$
# {\displaystyle {\begin{aligned}{dI_{\nu } \over d\tau _{\nu }}&={j_{\nu } \over \alpha _{\nu }}-I_{\nu }\\&=S_{\nu }-I_{\nu }\\\end{aligned}}\,\!}
# $$
# 
# where ${\displaystyle S_{\nu }}$ is a “source function”. In general,
# 
# 
# $$
# {\displaystyle S_{\nu }{\big |}_{scattering}\propto \int {I_{\nu }d\Omega }\,\!}
# $$

# There is a formal solution for $I_\nu$. Let's define $\hat{I} \equiv Ie^{-\tau_\nu}$ and $\hat{S} \equiv S e^{-\tau_\nu}$. Then: 
# 
# $$
# {\displaystyle {d{\tilde {I}} \over d\tau _{\nu }}={\tilde {S}}\,\!}
# $$
# 
# $$
# {\displaystyle {\tilde {I}}(\tau _{\nu })={\tilde {I}}(0)+\int _{0}^{\tau _{\nu }}{{\tilde {S}}~d{\tilde {\tau }}_{\nu }}\,\!}
# $$
# 
# $$
# {\displaystyle {I_{\nu }(\tau _{\nu })=\overbrace {I_{\nu }(0)e^{-\tau _{\nu }}} ^{background\ light}+\overbrace {\int _{0}^{\tau _{\nu }}{S_{\nu }(\tau _{\nu }^{\prime })\underbrace {e^{-(\tau _{\nu }-\tau _{\nu }^{\prime })}} _{self-absorption}d\tau _{\nu }^{\prime }}} ^{glowing\ medium}}\,\!}
# $$

# **If $S_\nu$ is constant with $\tau_\nu$, then:**
# 
# $$
# \boxed{{\displaystyle I_{\nu }(\tau _{\nu })=I_{\nu }(0)e^{-\tau _{\nu }}+S_{\nu }(1-e^{-\tau _{\nu }})\,\!}}
# $$

# That second term on the righthand side can be approximated as ${\displaystyle S_{\nu }\tau _{\nu }}$ for ${\displaystyle \tau _{\nu }\ll 1}$, since self-absorption is negligible. Similarly, for ${\displaystyle \tau _{\nu }\gg 1}$, it may be approximated as ${\displaystyle S_{\nu }}$. The source function ${\displaystyle S_{\nu }}$ is everything. It has both the absorption and emission coefficients embedded in it.

# ## Optical Depth

# Examples from [Astrobaki](https://casper.astro.berkeley.edu/astrobaki/index.php/Optical_Depth):

# ![](../figures/250px-Mona_lisa_vs_radius.png)
# 

# An example of the Mona Lisa at optical depth of ${\displaystyle \tau =0.1}$, for obscuring particles of various radii. To achieve the same optical depth, particles with a smaller cross-sectional area need to have a higher column density.

# ![](../figures/250px-Mona_lisa_vs_opt_depth.png)
# 
# 

# The Mona Lisa at various optical depths, illustrating how the transition from optically thin to optically thick erases the background picture.

# ![](../figures/250px-Fog.png)
# 
# 

# A useful real world example of optical depth is fog. Within a fog cloud, nearby objects are clearly visible and distant objects are completely obscured. At intermediate distances, objects are difficult but not impossible to discern. In this image, the tree to the left corresponds to an optical depth of approximately 1, since it is mostly obscured, though still visible. The person in the foreground is at an optical depth of less than 1 (perhaps around 0.5), since they are easily discernable and there is very little fog blocking light between the person and the observer. Lastly, the end of the road is at an optical depth much greater than 1, since it is completely covered over by the fog and invisible to the observer.
# 

# ## Takeaways

# * **Equation of Radiative Transfer**
# $$
# {\displaystyle {{dI_{\nu } \over ds}=j_{\nu }-\alpha _{\nu }I_{\nu }}\,\!}
# $$
# 
# * **EoRT in terms of Optical Depth:**
# $$
# {\displaystyle {\begin{aligned}{dI_{\nu } \over d\tau _{\nu }}&={j_{\nu } \over \alpha _{\nu }}-I_{\nu }\\&=S_{\nu }-I_{\nu }\\\end{aligned}}\,\!}
# $$
# 
# * $\alpha_\nu \equiv n \sigma_\nu \equiv \rho \kappa_\nu$ is the extinction coefficient with units of inverse length squared.
# 
# * $j_\nu$ is the emissivity and has units of specific intensity divided by length. 
# 
# * $S_\nu \equiv \frac{j_\nu}{\alpha_\nu}$ is the source function.
