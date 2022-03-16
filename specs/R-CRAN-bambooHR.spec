%global __brp_check_rpaths %{nil}
%global packname  bambooHR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Wrapper to the 'BambooHR' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-fs 

%description
Enables a user to consume the 'BambooHR' API endpoints using R. The actual
URL of the API will depend on your company domain, and will be handled by
the package automatically once you setup the config file. The API
documentation can be found here <https://documentation.bamboohr.com/docs>.

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
