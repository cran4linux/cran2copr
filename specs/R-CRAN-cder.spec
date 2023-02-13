%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cder
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the California Data Exchange Center (CDEC)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-lubridate >= 1.7
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-glue >= 1.3
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-dplyr >= 1.1
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-lubridate >= 1.7
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-glue >= 1.3
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-dplyr >= 1.1
Requires:         R-utils 

%description
Connect to the California Data Exchange Center (CDEC) Web Service
<http://cdec.water.ca.gov/>. 'CDEC' provides a centralized database to
store, process, and exchange real-time hydrologic information gathered by
various cooperators throughout California. The 'CDEC' Web Service
<http://cdec.water.ca.gov/dynamicapp/wsSensorData> provides a data
download service for accessing historical records.

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
