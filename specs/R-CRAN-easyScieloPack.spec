%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyScieloPack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Interface to Search 'SciELO' Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-httr >= 1.4.6
BuildRequires:    R-CRAN-xml2 >= 1.3.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rvest >= 1.0.3
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-httr >= 1.4.6
Requires:         R-CRAN-xml2 >= 1.3.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rvest >= 1.0.3
Requires:         R-stats 

%description
Provides a simple interface to search and retrieve scientific articles
from the 'SciELO' (Scientific Electronic Library Online) database
<https://scielo.org>. It allows querying, filtering, and visualizing
results in an interactive table.

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
