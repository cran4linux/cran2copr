%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalMixGPD
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Nonparametric Conditional Density Modeling in Causal Inference and Clustering with a Heavy-Tail Extension

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-nimble 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
The presence of a heavy tail is a feature of many scenarios when risk
management involves extremely rare events. While parametric distributions
may give adequate representation of the mode of data, they are likely to
misrepresent heavy tails, and completely nonparametric approaches lack a
rigorous mechanism for tail extrapolation; see Pickands (1975)
<doi:10.1214/aos/1176343003>. The package 'CausalMixGPD' implements the
semiparametric framework of Aich and Bhattacharya (2026)
<doi:10.5281/zenodo.19620523> for Bayesian analysis of heavy-tailed
outcomes by combining Dirichlet process mixture models for the body of the
distribution with optional generalized Pareto tails. The method allows for
unconditional and covariate-modulated mixtures, implements MCMC estimation
using 'nimble', and extends to mixtures of different arms' outcomes with
application to causal inference in the Rubin (1974) <doi:10.1037/h0037350>
framework. Posterior summaries include density functions, quantiles,
expected values, survival functions, and causal effects, with an emphasis
on tail quantiles and functional measures sensitive to the tail.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
