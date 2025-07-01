%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EIAapi
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Query Data from the 'EIA' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.8.2
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-jsonlite >= 1.8.2
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-dplyr >= 1.0.9

%description
Provides a function to query and extract data from the 'US Energy
Information Administration' ('EIA') API V2
<https://www.eia.gov/opendata/>. The 'EIA' API provides a variety of
information, in a time series format, about the energy sector in the US.
The API is open, free, and requires an access key and registration at
<https://www.eia.gov/opendata/>.

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
