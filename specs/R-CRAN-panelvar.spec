%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panelvar
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Vector Autoregression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.2.11
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-Matrix >= 1.2.11
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
We extend two general methods of moment estimators to panel vector
autoregression models (PVAR) with p lags of endogenous variables,
predetermined and strictly exogenous variables. This general PVAR model
contains the first difference GMM estimator by Holtz-Eakin et al. (1988)
<doi:10.2307/1913103>, Arellano and Bond (1991) <doi:10.2307/2297968> and
the system GMM estimator by Blundell and Bond (1998)
<doi:10.1016/S0304-4076(98)00009-8>. We also provide specification tests
(Hansen overidentification test, lag selection criterion and stability
test of the PVAR polynomial) and classical structural analysis for PVAR
models such as orthogonal and generalized impulse response functions,
bootstrapped confidence intervals for impulse response analysis and
forecast error variance decompositions.

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
