%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyPSID
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reading, Formatting, and Organizing the Panel Study of Income Dynamics (PSID)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-foreign >= 0.8.67
BuildRequires:    R-CRAN-LaF >= 0.6.0
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-foreign >= 0.8.67
Requires:         R-CRAN-LaF >= 0.6.0

%description
Provides various functions for reading and preparing the Panel Study of
Income Dynamics (PSID) for longitudinal analysis, including functions that
read the PSID's fixed width format files directly into R, rename all of
the PSID's longitudinal variables so that recurring variables have
consistent names across years, simplify assembling longitudinal datasets
from cross sections of the PSID Family Files, and export the resulting
PSID files into file formats common among other statistical programming
languages ('SAS', 'STATA', and 'SPSS').

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
