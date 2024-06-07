%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  admiraldev
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions and Development Tools for the Admiral Package Family

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.4
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-lifecycle >= 0.1.0
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.4
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-lifecycle >= 0.1.0
Requires:         R-CRAN-cli 

%description
Utility functions to check data, variables and conditions for functions
used in 'admiral' and 'admiral' extension packages. Additional utility
helper functions to assist developers with maintaining documentation,
testing and general upkeep of 'admiral' and 'admiral' extension packages.

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
