%global packname  confreq
%global packver   1.5.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Configural Frequencies Analysis Using Log-Linear Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-gmp 
Requires:         R-methods 

%description
Offers several functions for Configural Frequencies Analysis (CFA), which
is a useful statistical tool for the analysis of multiway contingency
tables. CFA was introduced by G. A. Lienert as 'Konfigurations Frequenz
Analyse - KFA'. Lienert, G. A. (1971). Die Konfigurationsfrequenzanalyse:
I. Ein neuer Weg zu Typen und Syndromen. Zeitschrift für Klinische
Psychologie und Psychotherapie, 19(2), 99–115.

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
