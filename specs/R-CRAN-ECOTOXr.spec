%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ECOTOXr
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Extract Data from US EPA's ECOTOX Database

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-dbplyr >= 2.4.0
BuildRequires:    R-CRAN-RSQLite >= 2.3.4
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-crayon >= 1.5.2
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-rvest >= 1.0.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.3
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-dbplyr >= 2.4.0
Requires:         R-CRAN-RSQLite >= 2.3.4
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-crayon >= 1.5.2
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-rvest >= 1.0.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-rappdirs >= 0.3.3
Requires:         R-utils 

%description
The US EPA ECOTOX database is a freely available database with a treasure
of aquatic and terrestrial ecotoxicological data. As the online search
interface doesn't come with an API, this package provides the means to
easily access and search the database in R. To this end, all raw tables
are downloaded from the EPA website and stored in a local SQLite database.

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
