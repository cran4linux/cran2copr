%global packname  sapa
%global packver   2.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spectral Analysis for Physical Applications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-ifultools >= 2.0.22
BuildRequires:    R-CRAN-splus2R >= 1.3.3
BuildRequires:    R-methods 
Requires:         R-CRAN-ifultools >= 2.0.22
Requires:         R-CRAN-splus2R >= 1.3.3
Requires:         R-methods 

%description
Software for book "Spectral Analysis for Physical Applications", Donald B.
Percival and Andrew T. Walden (1993), <doi:10.1017/CBO9780511622762>,
Cambridge University Press. Contains functionality for nonparametric
spectral density estimation of time series, including direct spectral
estimators, lag window estimators, estimators based on Welch's overlapped
segment averaging (WOSA) and multitaper estimators based on discrete
prolate spheroidal sequences (DPSS) and on sinusoidal tapers.

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
