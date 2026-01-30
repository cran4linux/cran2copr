%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  readepi
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Read Data from Relational Database Management Systems and Health Information Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-odbc 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-odbc 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-tidyr 

%description
Import Data from Relational Database Management Systems (RDBMS) and Health
Information Systems ('HIS'). The current version of the package supports
importing data from RDBMS including 'MS SQL', 'MySQL', 'PostGRESQL', and
'SQLite', as well as from two HIS platforms: 'DHIS2' and 'SORMAS'.

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
