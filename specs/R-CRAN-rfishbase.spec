%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rfishbase
%global packver   4.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'FishBase'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-contentid >= 0.0.15
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-contentid >= 0.0.15
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 

%description
A programmatic interface to 'FishBase', re-written based on an
accompanying 'RESTful' API. Access tables describing over 30,000 species
of fish, their biology, ecology, morphology, and more. This package also
supports experimental access to 'SeaLifeBase' data, which contains nearly
200,000 species records for all types of aquatic life not covered by
'FishBase.'

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
