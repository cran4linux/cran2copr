%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rilostat
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Manipulation of ILOSTAT Labour Statistics

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-haven >= 2.5.0
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-stringr >= 1.5.2
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-haven >= 2.5.0
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-stringr >= 1.5.2
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0

%description
Provides functions to access and manipulate data from the ILOSTAT database
<https://ilostat.ilo.org>, the International Labour Organization's
repository of labour statistics. Supports bulk download of datasets,
metadata retrieval, and tools for filtering, reshaping, and analysing
data.

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
