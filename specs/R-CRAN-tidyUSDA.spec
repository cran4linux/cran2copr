%global __brp_check_rpaths %{nil}
%global packname  tidyUSDA
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Minimal Tool Set for Gathering USDA Quick Stat Data for Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-tigris >= 1.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fuzzyjoin 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-waldo 
BuildRequires:    R-CRAN-diffobj 
BuildRequires:    R-CRAN-gitcreds 
Requires:         R-CRAN-tigris >= 1.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fuzzyjoin 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-brio 
Requires:         R-CRAN-waldo 
Requires:         R-CRAN-diffobj 
Requires:         R-CRAN-gitcreds 

%description
Provides a consistent API to pull United States Department of Agriculture
census and survey data from the National Agricultural Statistics Service
(NASS) QuickStats service.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
