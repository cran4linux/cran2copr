%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clockify
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Wrapper for the 'Clockify' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
A wrapper for the Clockify API <https://docs.clockify.me/>, making it
possible to query, insert and update time keeping data.

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
