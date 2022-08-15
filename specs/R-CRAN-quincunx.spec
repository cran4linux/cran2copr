%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quincunx
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          REST API Client for the 'PGS' Catalog

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyjson 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-concatenate 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyjson 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-progress 
Requires:         R-methods 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-concatenate 
Requires:         R-CRAN-memoise 

%description
Programmatic access to the 'PGS' Catalog. This package provides easy
access to 'PGS' Catalog data by accessing the REST API
<https://www.pgscatalog.org/rest/>.

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
