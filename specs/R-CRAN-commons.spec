%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  commons
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          AI Agents for Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-ellmer >= 0.4.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-utils 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-ellmer >= 0.4.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-S7 
Requires:         R-utils 

%description
Implements large language model agents for answering questions about
database tables. Agents combine 'DBI' database connections with table and
column metadata from a data dictionary
(<https://data-dict.tidyverse.org/>), using registered calculations when
applicable and generating database queries otherwise. They can also be
embedded in a 'Shiny' application.

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
