%global __brp_check_rpaths %{nil}
%global packname  podr
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Common Functions for 'PHUSE' Open Data Repository

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-odbc >= 1.2.3
BuildRequires:    R-CRAN-RPostgres >= 1.2.1
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-plogr >= 0.2.0
BuildRequires:    R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-odbc >= 1.2.3
Requires:         R-CRAN-RPostgres >= 1.2.1
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-plogr >= 0.2.0
Requires:         R-CRAN-rstudioapi >= 0.10

%description
Make it easy to connect, access and review datasets in Pharmaceutical User
Software Exchange ('PHUSE') open data repository ('PODR'). The R Shiny
application included in this package allow users to connect to 'PODR' and
access to over 260 open data sets.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
