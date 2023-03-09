%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taxadb
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A High-Performance Local Taxonomic Database Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-contentid 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-contentid 
Requires:         R-CRAN-memoise 

%description
Creates a local database of many commonly used taxonomic authorities and
provides functions that can quickly query this data.

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
