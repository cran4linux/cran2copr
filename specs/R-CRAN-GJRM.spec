%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GJRM
%global packver   0.2-6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6.8
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Joint Regression Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-distrEx 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-VineCopula 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ismev 
Requires:         R-methods 
Requires:         R-CRAN-distrEx 

%description
Routines for fitting various joint (and univariate) regression models,
with several types of covariate effects, in the presence of equations'
errors association.

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
