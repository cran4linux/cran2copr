%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cansim
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Accessing Statistics Canada Data Table and Vectors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-utils >= 4.3
BuildRequires:    R-CRAN-tibble >= 3.2
BuildRequires:    R-CRAN-dbplyr >= 2.5
BuildRequires:    R-CRAN-RSQLite >= 2.3
BuildRequires:    R-CRAN-readr >= 2.1
BuildRequires:    R-CRAN-arrow >= 18.1
BuildRequires:    R-CRAN-stringr >= 1.5
BuildRequires:    R-CRAN-tidyr >= 1.3
BuildRequires:    R-CRAN-DBI >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.1
BuildRequires:    R-CRAN-rlang >= 1.1
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0
BuildRequires:    R-CRAN-digest >= 0.6
Requires:         R-utils >= 4.3
Requires:         R-CRAN-tibble >= 3.2
Requires:         R-CRAN-dbplyr >= 2.5
Requires:         R-CRAN-RSQLite >= 2.3
Requires:         R-CRAN-readr >= 2.1
Requires:         R-CRAN-arrow >= 18.1
Requires:         R-CRAN-stringr >= 1.5
Requires:         R-CRAN-tidyr >= 1.3
Requires:         R-CRAN-DBI >= 1.2
Requires:         R-CRAN-dplyr >= 1.1
Requires:         R-CRAN-rlang >= 1.1
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0
Requires:         R-CRAN-digest >= 0.6

%description
Searches for, accesses, and retrieves Statistics Canada data tables, as
well as individual vectors, as tidy data frames. This package enriches the
tables with metadata, deals with encoding issues, allows for bilingual
English or French language data retrieval, and bundles convenience
functions to make it easier to work with retrieved table data. For more
efficient data access the package allows for caching data in a local
database and database level filtering, data manipulation and summarizing.

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
