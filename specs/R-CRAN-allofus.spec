%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  allofus
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for 'All of Us' Researcher Workbench

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 2.5.0
BuildRequires:    R-CRAN-bigrquery >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-bit64 
Requires:         R-CRAN-dbplyr >= 2.5.0
Requires:         R-CRAN-bigrquery >= 1.5.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-bit64 

%description
Streamline use of the 'All of Us' Researcher Workbench
(<https://www.researchallofus.org/data-tools/workbench/>)with tools to
extract and manipulate data from the 'All of Us' database. Increase
interoperability with the Observational Health Data Science and
Informatics ('OHDSI') tool stack by decreasing reliance of 'All of Us'
tools and allowing for cohort creation via 'Atlas'. Improve reproducible
and transparent research using 'All of Us'.

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
