%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RDML7
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Read, Write, Validate, and Analyze Real-Time PCR Data in the 'RDML' Format

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.6.2
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-xml2 >= 1.0
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
Requires:         R-CRAN-checkmate >= 1.6.2
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-xml2 >= 1.0
Requires:         R-CRAN-S7 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-tools 

%description
Reads, writes, validates, converts, and manipulates quantitative
polymerase chain reaction (qPCR) data through the Real-Time PCR Data
Markup Language ('RDML') application programming interface (API), using
'S7' objects. Includes an extensible file-format registry, vendor and
tabular-data importers, 'RDES' import and export, fluorescence-table
helpers, semantic validation, and compatibility wrappers for the
historical 'RDML' API.

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
