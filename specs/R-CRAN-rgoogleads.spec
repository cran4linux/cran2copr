%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgoogleads
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Loading Data from 'Google Ads API'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-gargle >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-gargle >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-rappdirs 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Interface for loading data from 'Google Ads API', see
<https://developers.google.com/google-ads/api/docs/start>. Package provide
function for authorization and loading reports.

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
