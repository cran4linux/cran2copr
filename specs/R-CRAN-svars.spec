%global __brp_check_rpaths %{nil}
%global packname  svars
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Data-Driven Identification of SVAR Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-vars >= 1.5.3
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-steadyICA 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-vars >= 1.5.3
Requires:         R-CRAN-expm 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-steadyICA 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-Rcpp 

%description
Implements data-driven identification methods for structural vector
autoregressive (SVAR) models as described in Lange et al. (2021)
<doi:10.18637/jss.v097.i05>. Based on an existing VAR model object
(provided by e.g. VAR() from the 'vars' package), the structural impact
matrix is obtained via data-driven identification techniques (i.e. changes
in volatility (Rigobon, R. (2003) <doi:10.1162/003465303772815727>),
patterns of GARCH (Normadin, M., Phaneuf, L. (2004)
<doi:10.1016/j.jmoneco.2003.11.002>), independent component analysis
(Matteson, D. S, Tsay, R. S., (2013) <doi:10.1080/01621459.2016.1150851>),
least dependent innovations (Herwartz, H., Ploedt, M., (2016)
<doi:10.1016/j.jimonfin.2015.11.001>), smooth transition in variances
(Luetkepohl, H., Netsunajev, A. (2017) <doi:10.1016/j.jedc.2017.09.001>)
or non-Gaussian maximum likelihood (Lanne, M., Meitz, M., Saikkonen, P.
(2017) <doi:10.1016/j.jeconom.2016.06.002>)).

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
