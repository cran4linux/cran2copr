%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  L0ggm
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Smooth L0 Penalty Approximations for Gaussian Graphical Models

License:          AGPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glassoFast 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-stats 

%description
Provides smooth approximations to the L0 norm penalty for estimating
sparse Gaussian graphical models (GGMs). Network estimation is performed
using the Local Linear Approximation (LLA) framework (Fan & Li, 2001
<doi:10.1198/016214501753382273>; Zou & Li, 2008
<doi:10.1214/009053607000000802>) with five penalty functions: arctangent
(Wang & Zhu, 2016 <doi:10.1155/2016/6495417>), EXP (Wang, Fan, & Zhu, 2018
<doi:10.1007/s10463-016-0588-3>), Gumbel, Log (Candes, Wakin, & Boyd, 2008
<doi:10.1007/s00041-008-9045-x>), and Weibull. Adaptive penalty parameters
for EXP, Gumbel, and Weibull are estimated via maximum likelihood, and
model selection uses information criteria including AIC, BIC, and EBIC
(Extended BIC). Simulation functions generate multivariate normal data
from GGMs with stochastic block model or small-world (Watts-Strogatz)
network structures.

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
