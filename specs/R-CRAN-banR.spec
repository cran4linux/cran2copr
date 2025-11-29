%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  banR
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the 'BAN' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
A client for the 'Base Adresses Nationale' ('BAN') API, which allows to
(batch) geocode and reverse-geocode French addresses. For more information
about the 'BAN' and its API, please see
<https://adresse.data.gouv.fr/outils/api-doc/adresse>.

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
