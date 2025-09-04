%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigrquery
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to Google's 'BigQuery' 'API'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-gargle >= 1.5.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-nanoparquet >= 0.3.1
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clock 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cpp11 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-gargle >= 1.5.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-nanoparquet >= 0.3.1
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-brio 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clock 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-prettyunits 
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
