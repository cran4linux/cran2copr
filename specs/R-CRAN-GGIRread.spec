%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GGIRread
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wearable Accelerometer Data File Readers

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 

%description
Reads data collected from wearable acceleratometers as used in sleep and
physical activity research. Currently supports file formats: binary data
from 'GENEActiv' <https://activinsights.com/>, .bin-format from GENEA
devices (not for sale), and .cwa-format from 'Axivity'
<https://axivity.com>. Further, it has functions for reading text files
with epoch level aggregates from 'Actical', 'Fitbit', 'Actiwatch',
'ActiGraph', and 'PhilipsHealthBand'. Primarily designed to complement R
package GGIR <https://CRAN.R-project.org/package=GGIR>.

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
