%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cansim
%global packver   0.3.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.17
Release:          1%{?dist}%{?buildtag}
Summary:          Accessing Statistics Canada Data Table and Vectors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-digest >= 0.1
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-digest >= 0.1
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 

%description
Searches for, accesses, and retrieves new-format and old-format Statistics
Canada data tables, as well as individual vectors, as tidy data frames.
This package deals with encoding issues, allows for bilingual English or
French language data retrieval, and bundles convenience functions to make
it easier to work with retrieved table data. Optional caching features are
provided.

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
