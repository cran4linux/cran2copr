%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datagovsgR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Call Real Time APIs from Data Gov Singapore

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 

%description
A wrapper for the Data.gov.sg developer resources, which provide real time
and historical information, ranging from carpark availability to weather
forecasts. The functions makes the API calls for a given date and time,
before returning the relevant information in a data frame. All APIs are
supported, less the IPOS one which is not returning any data. Relevant
information can be found here <https://data.gov.sg/developer>.

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
