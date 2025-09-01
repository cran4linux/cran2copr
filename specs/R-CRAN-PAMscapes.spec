%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAMscapes
%global packver   0.14.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Summarising and Analysing Soundscape Data

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-PAMmisc >= 1.12.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-tdigest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-PAMmisc >= 1.12.4
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-tdigest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-DT 

%description
A variety of tools relevant to the analysis of marine soundscape data.
There are tools for downloading AIS (automatic identification system) data
from Marine Cadastre <https://hub.marinecadastre.gov>, connecting AIS data
to GPS coordinates, plotting summaries of various soundscape measurements,
and downloading relevant environmental variables (wind, swell height) from
the National Center for Atmospheric Research data server
<https://rda.ucar.edu/datasets/ds084.1/>. Most tools were developed to
work well with output from 'Triton' software, but can be adapted to work
with any similar measurements.

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
