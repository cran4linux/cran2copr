%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SunCalcMeeus
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sun Position and Daylight Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-lubridate >= 1.9.3
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-stats 
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-lubridate >= 1.9.3
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-stats 

%description
Compute the position of the sun, and local solar time using Meeus'
formulae. Compute day and/or night length using different twilight
definitions or arbitrary sun elevation angles. This package is part of the
'r4photobiology' suite, Aphalo, P. J. (2015)
<doi:10.19232/uv4pb.2015.1.14>. Algorithms from Meeus (1998,
ISBN:0943396611).

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
