%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eppoFindeR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the EPPO Database and Public APIs

License:          EUPL-1.2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.5
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-checkmate >= 2.3.1
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-glue >= 1.7.0
BuildRequires:    R-CRAN-httr2 >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-cli >= 3.6.5
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-checkmate >= 2.3.1
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-glue >= 1.7.0
Requires:         R-CRAN-httr2 >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.2

%description
Provides an interface to the public APIs of the European and Mediterranean
Plant Protection Organization (EPPO) database. It enables users to
retrieve EPPO data by accessing specific services and datasets. The
package also includes utilities for data wrangling, including the
integration of taxonomy with rank information. See
<https://data.eppo.int/apis/> for more details.

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
