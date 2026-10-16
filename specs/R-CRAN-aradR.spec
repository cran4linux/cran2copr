%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aradR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modern R Client and Toolkit for the Czech National Bank ARAD API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 0.2.2
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-httr2 >= 0.2.2
Requires:         R-CRAN-curl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 

%description
Provides a reliability-first interface to the public Czech National Bank
ARAD API for discovering indicators, browsing human-readable metadata,
retrieving and validating time series, working with dimensions and
snapshots, reshaping data, and building reproducible data workflows. The
package is designed for robust handling of long requests, parsing
diagnostics, missing values, retries, caching, and automated tests.

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
