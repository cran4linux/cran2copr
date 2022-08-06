%global __brp_check_rpaths %{nil}
%global packname  R2WinBUGS
%global packver   2.1-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.21
Release:          1%{?dist}%{?buildtag}
Summary:          Running 'WinBUGS' and 'OpenBUGS' from 'R' / 'S-PLUS'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         openbugs
BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda >= 0.11.0
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-coda >= 0.11.0
Requires:         R-CRAN-boot 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Invoke a 'BUGS' model in 'OpenBUGS' or 'WinBUGS', a class "bugs" for
'BUGS' results and functions to work with that class. Function
write.model() allows a 'BUGS' model file to be written. The class and
auxiliary functions could be used with other MCMC programs, including
'JAGS'.

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
