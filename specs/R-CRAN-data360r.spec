%global __brp_check_rpaths %{nil}
%global packname  data360r
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper for 'TCdata360' and 'Govdata360' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 

%description
Makes it easy to engage with the Application Program Interface (API) of
the 'TCdata360' and 'Govdata360' platforms at
<https://tcdata360.worldbank.org/> and
<https://govdata360.worldbank.org/>, respectively. These application
program interfaces provide access to over 5000 trade, competitiveness, and
governance indicator data, metadata, and related information from sources
both inside and outside the World Bank Group. Package functions include
easier download of data sets, metadata, and related information, as well
as searching based on user-inputted query.

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
