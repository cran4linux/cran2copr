%global __brp_check_rpaths %{nil}
%global packname  cplm
%global packver   0.7-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.9
Release:          1%{?dist}%{?buildtag}
Summary:          Compound Poisson Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-biglm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-tweedie 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 
Requires:         R-methods 
Requires:         R-CRAN-biglm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-tweedie 

%description
Likelihood-based and Bayesian methods for various compound Poisson linear
models based on Zhang, Yanwei (2013)
<https://link.springer.com/article/10.1007/s11222-012-9343-7>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
