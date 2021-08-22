%global __brp_check_rpaths %{nil}
%global packname  onc.api
%global packver   2.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Oceans 2.0 API Client Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-humanize 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-humanize 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-crayon 
Requires:         R-utils 
Requires:         R-CRAN-testthat 

%description
Allows users to discover and retrieve Ocean Networks Canada's
oceanographic data in raw, text, image, audio, video or any other format
available. Provides a class that wraps web service calls and business
logic so that users can download data with a single line of code.

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
