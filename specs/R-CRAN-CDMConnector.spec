%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CDMConnector
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connect to an OMOP Common Data Model

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 2.5.0
BuildRequires:    R-CRAN-omopgenerics >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 0.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-dbplyr >= 2.5.0
Requires:         R-CRAN-omopgenerics >= 1.2.0
Requires:         R-CRAN-DBI >= 0.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 

%description
Provides tools for working with observational health data in the
Observational Medical Outcomes Partnership (OMOP) Common Data Model format
with a pipe friendly syntax. Common data model database table references
are stored in a single compound object along with metadata.

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
