%global __brp_check_rpaths %{nil}
%global packname  ARpLMEC
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Censored Mixed-Effects Models with Different Correlation Structures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lmec 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-MomTrunc 
BuildRequires:    R-CRAN-TTmoment 
BuildRequires:    R-CRAN-relliptical 
Requires:         R-CRAN-Matrix 
Requires:         R-stats4 
Requires:         R-CRAN-gmm 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lmec 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-MomTrunc 
Requires:         R-CRAN-TTmoment 
Requires:         R-CRAN-relliptical 

%description
Left, right or interval censored mixed-effects linear model with
autoregressive errors of order p or DEC correlation structure using the
type-EM algorithm. The error distribution can be Normal or t-Student. It
provides the parameter estimates, the standard errors and prediction of
future observations (available only for the normal case). Olivari et all
(2021) <doi:10.1080/10543406.2020.1852246>.

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
