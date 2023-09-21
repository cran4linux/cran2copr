%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ie2misc
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Irucka Embry's Miscellaneous USGS Functions

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1.4
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.10.2
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-mgsub 
BuildRequires:    R-CRAN-reader 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-openxlsx >= 4.1.4
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-data.table >= 1.10.2
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-mgsub 
Requires:         R-CRAN-reader 
Requires:         R-CRAN-lubridate 
Requires:         R-tcltk 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-checkmate 

%description
A collection of Irucka Embry's miscellaneous USGS functions (processing
.exp and .psf files, statistical error functions, "+" dyadic operator for
use with NA, creating ADAPS and QW spreadsheet files, calculating
saturated enthalpy). Irucka created these functions while a Cherokee
Nation Technology Solutions (CNTS) United States Geological Survey (USGS)
Contractor and/or USGS employee.

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
