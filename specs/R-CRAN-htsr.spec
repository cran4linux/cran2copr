%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  htsr
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hydro-Meteorology Time-Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-WriteXLS 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-editData 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-WriteXLS 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-editData 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-terra 

%description
Functions for the management and treatment of hydrology and meteorology
time-series stored in a 'Sqlite' data base.

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
