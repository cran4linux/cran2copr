%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  photobiologyInOut
%global packver   0.4.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.30
Release:          1%{?dist}%{?buildtag}
Summary:          Read Spectral and Logged Data from Foreign Files

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-colorSpec >= 1.5.0
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-anytime >= 0.3.9
BuildRequires:    R-CRAN-photobiology >= 0.11.4
BuildRequires:    R-CRAN-SunCalcMeeus >= 0.1.1
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-colorSpec >= 1.5.0
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-anytime >= 0.3.9
Requires:         R-CRAN-photobiology >= 0.11.4
Requires:         R-CRAN-SunCalcMeeus >= 0.1.1
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 

%description
Functions for reading, and in some cases writing, foreign files containing
spectral data from spectrometers and their associated software, output
from daylight simulation models in common use, and some spectral data
repositories. As well as functions for exchange of spectral data with
other R packages. Part of the 'r4photobiology' suite, Aphalo P. J. (2015)
<doi:10.19232/uv4pb.2015.1.14>.

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
