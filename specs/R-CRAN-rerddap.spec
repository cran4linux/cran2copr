%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rerddap
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          General Purpose Client for 'ERDDAP' Servers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-ncdf4 >= 1.16
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-crul >= 0.7
BuildRequires:    R-CRAN-hoardr >= 0.5.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-ncdf4 >= 1.16
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-crul >= 0.7
Requires:         R-CRAN-hoardr >= 0.5.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-tibble 

%description
General purpose R client for 'ERDDAP' servers. Includes functions to
search for 'datasets', get summary information on 'datasets', and fetch
'datasets', in either 'csv' or 'netCDF' format. 'ERDDAP' information:
<https://upwell.pfeg.noaa.gov/erddap/information.html>.

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
