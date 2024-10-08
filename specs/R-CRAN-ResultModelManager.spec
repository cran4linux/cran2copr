%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ResultModelManager
%global packver   0.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          Result Model Manager

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 6.0.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-SqlRender 
BuildRequires:    R-CRAN-ParallelLogger 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-DatabaseConnector >= 6.0.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-SqlRender 
Requires:         R-CRAN-ParallelLogger 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-withr 

%description
Database data model management utilities for R packages in the
Observational Health Data Sciences and Informatics program
<https://ohdsi.org>. 'ResultModelManager' provides utility functions to
allow package maintainers to migrate existing SQL database models, export
and import results in consistent patterns.

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
