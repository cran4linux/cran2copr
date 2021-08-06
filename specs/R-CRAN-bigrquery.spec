%global __brp_check_rpaths %{nil}
%global packname  bigrquery
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to Google's 'BigQuery' 'API'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-gargle >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-gargle >= 1.2.0
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 

%description
Easily talk to Google's 'BigQuery' database from R.

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
