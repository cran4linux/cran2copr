%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  electionsBR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Functions to Download and Clean Brazilian Electoral Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-haven >= 1.0.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-haven >= 1.0.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 

%description
Offers a set of functions to easily download and clean Brazilian electoral
data from the Superior Electoral Court and 'CepespData' websites. Among
other features, the package retrieves data on local and federal elections
for all positions (city councilor, mayor, state deputy, federal deputy,
governor, and president) aggregated by state, city, and electoral zones.

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
