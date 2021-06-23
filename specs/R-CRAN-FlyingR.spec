%global __brp_check_rpaths %{nil}
%global packname  FlyingR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Bird Flight Range

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-rmarkdown 

%description
Functions for range estimation in birds based on Pennycuick (2008) and
Pennycuick (1975), 'Flight' program which compliments Pennycuick (2008)
requires manual entry of birds which can be tedious when there are
hundreds of birds to estimate. Implemented are two ODE methods discussed
in Pennycuick (1975) and time-marching computation methods as in
Pennycuick (1998) and Pennycuick (2008). See Pennycuick (1975,
ISBN:978-0-12-249405-5), Pennycuick (1998) <doi:10.1006/jtbi.1997.0572>,
and Pennycuick (2008, ISBN:9780080557816).

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
