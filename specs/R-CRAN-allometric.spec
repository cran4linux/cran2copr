%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  allometric
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Structured Allometric Models for Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-RefManageR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ISOcodes 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-units 
Requires:         R-CRAN-RefManageR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ISOcodes 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-curl 

%description
Access allometric models used in forest resource analysis, such as volume
equations, taper equations, biomass models, among many others. Users are
able to efficiently find and select allometric models suitable for their
project area and use them in analysis. Additionally, 'allometric' provides
a structured framework for adding new models to an open-source models
repository.

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
