%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigrquerystorage
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to Google's 'BigQuery Storage' API

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-bigrquery 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-arrow 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-bigrquery 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-tibble 

%description
Easily talk to Google's 'BigQuery Storage' API from R
(<https://cloud.google.com/bigquery/docs/reference/storage/rpc>).

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
