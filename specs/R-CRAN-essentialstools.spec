%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  essentialstools
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Datasets and Utilities for Essentials of Statistics for the Behavioral Sciences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-WebPower 
BuildRequires:    R-CRAN-pwr 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-WebPower 
Requires:         R-CRAN-pwr 

%description
Provides instructional datasets and simple wrapper functions for selected
analyses used in 'Essentials of Statistics for the Behavioral Sciences'.
The package is intended to support textbook examples by distributing data
in a form that is easy for students and instructors to access within R.
Current functionality includes packaged datasets and convenience wrappers
for functions from 'ez', 'pwr', and 'WebPower' for analysis of variance
and statistical power calculations. The package is designed as a companion
resource for teaching and learning in introductory and intermediate
statistics courses.

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
